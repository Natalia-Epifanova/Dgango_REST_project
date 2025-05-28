from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserRetrieveAPIView, UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, \
    UserListAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"payments", PaymentViewSet, basename="payments")

urlpatterns = [
    path("list/", UserListAPIView.as_view(), name="users_list"),
    path("profile/", UserRetrieveAPIView.as_view(), name="profile"),
    path("profile/update/", UserUpdateAPIView.as_view(), name="profile_update"),
    path("profile/delete/", UserDeleteAPIView.as_view(), name="profile_delete"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
