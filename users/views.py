from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from materials.models import Course
from users.models import Payments, User, Subscription
from users.permissions import IsProfileOwner
from users.serializers import (
    PaymentSerializer,
    UserPrivateSerializer,
    UserPublicSerializer,
)


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPrivateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        password = serializer.validated_data.get("password")
        print(f"Creating user with password: {password}")
        user = serializer.save(is_active=True)
        user.set_password(password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):

    def get_serializer_class(self):
        if self.request.user == self.get_object():
            return UserPrivateSerializer
        return UserPublicSerializer

    def get_object(self):
        return User.objects.get(pk=self.kwargs["pk"])


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserPrivateSerializer
    permission_classes = [IsAuthenticated, IsProfileOwner]

    def get_object(self):
        return self.request.user


class UserListAPIView(ListAPIView):
    serializer_class = UserPublicSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["paid_course", "paid_lesson", "payment_method"]
    ordering_fields = ["payment_date"]


class SubscriptionAPIView(APIView):

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get("course_id")
        if not course_id:
            return Response({"error": "course_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        course_item = get_object_or_404(Course, id=course_id)

        subs_item, created = Subscription.objects.get_or_create(
            user=user,
            course=course_item,
            defaults={"user": user, "course": course_item},
        )

        if not created:
            subs_item.delete()
            message = "Подписка удалена"
        else:
            message = "Подписка добавлена"

        return Response({"message": message}, status=status.HTTP_200_OK)
