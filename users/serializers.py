from rest_framework import serializers
from users.models import Payments, User
from materials.models import Course, Lesson


class PaymentSerializer(serializers.ModelSerializer):
    paid_course = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Course.objects.all(),
        required=False,
        allow_null=True,
    )
    paid_lesson = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Lesson.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payment_history = serializers.SerializerMethodField()

    def get_payment_history(self, obj):
        payments = obj.payments.all().order_by("-payment_date")
        return PaymentSerializer(payments, many=True).data

    class Meta:
        model = User
        fields = ["email", "phone", "city", "avatar", "payment_history"]
