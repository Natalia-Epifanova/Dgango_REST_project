from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserProfileView, UserRegistrationAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("register/", UserRegistrationAPIView.as_view(), name="user-register"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
] + router.urls
