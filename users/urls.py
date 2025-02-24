from django.urls import path
from .views import AccountCreateView, PassportDataSerializer, PassportDataDetailsView, CustomTokenObtainPairView
from django.urls import path
from .views import GenerateOTPView, VerifyOTPView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('generate_otp/', GenerateOTPView.as_view(), name='generate_otp'),
    path('verify_otp/', VerifyOTPView.as_view(), name='verify_otp'),
    path("account/", AccountCreateView.as_view(), name="account-create"),
    path("user-details/", PassportDataDetailsView.as_view(), name="user-details"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),  # Login & get access/refresh tokens
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Get new access token using refresh token
    path("logout/", TokenBlacklistView.as_view(), name="token_blacklist"),  # Logout by blacklisting refresh token
]


