from django.urls import path
from auth.views import (
    RegisterView, ChangePasswordView, UpdateProfileView, LogoutView,
    UpdateUserImageView, ResetPasswordView,
    ValidateConfirmationCodeView, ForgotPasswordView)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

app_name = 'auth'

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('register/', RegisterView.as_view(), name='auth_register'),

    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('upload_image/<int:pk>/', UpdateUserImageView.as_view(), name='auth_image'),

    path('forgot_password/', ForgotPasswordView.as_view(), name='auth_forgot_password'),
    path('confirm/', ValidateConfirmationCodeView.as_view(), name='auth_confirm'),
    path('reset_password/<int:pk>/', ResetPasswordView.as_view(), name='auth_reset_password'),

    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

    path('logout/', LogoutView.as_view(), name='auth_logout'),
]

