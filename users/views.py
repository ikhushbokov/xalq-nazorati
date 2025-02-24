# from allauth.account.templatetags import account
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from datetime import timedelta
import random

from .models import PassportData, Account
from .serializers import PassportDataSerializer, AccountSerializer


class GenerateOTPView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({"error": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            account = Account.objects.get(phone_number=phone_number)
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        otp = account.generate_otp()
        return Response({"otp": otp}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')

        if not phone_number or not otp:
            return Response({"error": "Phone number and OTP are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            account = Account.objects.get(phone_number=phone_number)
        except Account.DoesNotExist:
            return Response({"error": "Account not found."}, status=status.HTTP_404_NOT_FOUND)

        if account.is_otp_valid(otp):
            # OTP is correct, issue JWT token
            refresh = RefreshToken.for_user(account)
            return Response({
                "message": "OTP verified successfully!",
                "access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)



class AccountCreateView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # def post(self, request):
    #     serializer = AccountSerializer(data=request.data)
    #
    #     if serializer.is_valid():
    #         account = serializer.save()
    #
    #         otp, _ = OTP.objects.get_or_create(user=account, phone_number=account.phone_number)
    #         otp.generate_otp()
    #
    #         return Response({
    #             "phone_number": account.phone_number,
    #             "otp_code": otp.otp_code
    #         }, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PassportDataDetailsView(generics.UpdateAPIView):
    queryset = PassportData.objects.all()
    serializer_class = PassportDataSerializer


class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get("phone_number")
        otp = request.data.get("otp")

        # Verify OTP here, and if valid:
        user = get_user_model().objects.filter(phone_number=phone_number).first()

        if user and user.verify_otp(otp):  # Assuming you have an OTP verification method
            # Generate token manually or let Simple JWT do it for you
            from rest_framework_simplejwt.tokens import RefreshToken

            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"detail": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)
