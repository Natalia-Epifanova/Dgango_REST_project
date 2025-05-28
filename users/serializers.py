from rest_framework import serializers

from materials.models import Course, Lesson
from users.models import Payments, User


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

    @staticmethod
    def get_payment_history(obj):
        payments = obj.payments.all().order_by("-payment_date")
        return PaymentSerializer(payments, many=True).data

    class Meta:
        model = User
        fields = ["email", "phone", "city", "avatar", "payment_history"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            phone=validated_data.get("phone", ""),
            city=validated_data.get("city", ""),
            avatar=validated_data.get("avatar", None),
        )
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "city", "avatar"]
