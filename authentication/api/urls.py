from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.api.views.change_password_view import ChangePasswordAPIView
from authentication.api.views.login_view import LoginAPIView
from authentication.api.views.register_view import RegisterAPIView
from authentication.api.views.reset_password_view import (
    SendResetPasswordToken,
    VerifyResetPasswordTokenAPIView
)

urlpatterns = [
    # JWT
    path('token/create/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # Register
    path('register/', RegisterAPIView.as_view(), name='register-user'),
    # Login
    path('login/', LoginAPIView.as_view(), name='login-user'),
    # Change Password
    path('change-password/', ChangePasswordAPIView.as_view(), name='change-password-user'),
    # Reset Password
    path('reset-password/send/', SendResetPasswordToken.as_view(), name='send-reset-password'),
    path('reset-password/verify/', VerifyResetPasswordTokenAPIView.as_view(), name='verify-reset-password'),
]
