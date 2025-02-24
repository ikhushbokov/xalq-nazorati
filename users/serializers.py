from rest_framework import serializers
from .models import Account, PassportData


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone_number', 'name', 'is_active', 'is_staff', 'created_time']

    def validate_phone_number(self, value):
        if not value.startswith('998'):
            raise serializers.ValidationError("Phone number must start with '998'.")
        if len(value) != 12:
            raise serializers.ValidationError("Phone number must be exactly 12 digits long.")
        if Account.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("Phone number already exists.")
        return value

class PassportDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportData
        fields = ["passport", "birth_date"]  # Second endpoint to collect user details


