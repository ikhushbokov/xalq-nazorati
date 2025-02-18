from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'phone_number', 'full_name', 'passport')