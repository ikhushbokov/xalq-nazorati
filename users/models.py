from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import random
import string
from datetime import timedelta
from django.utils import timezone


class AccountManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field is required")

        account = self.model(phone_number=phone_number, **extra_fields)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(phone_number, password, **extra_fields)


from django.core.exceptions import ValidationError

class Account(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)  # Add expiry field

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    objects = AccountManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return self.phone_number

    def generate_otp(self):
        """Generate a 6-digit OTP and store it with an expiration time."""
        otp = str(random.randint(100000, 999999))
        self.otp = otp
        self.otp_expiry = timezone.now() + timedelta(minutes=5)
        self.save()
        return otp


    def verify_otp(self, otp_input):
        """Verify the OTP input by the user."""
        if self.otp == otp_input:
            return True
        return False

    def is_otp_valid(self, otp):
        """Check if the OTP is valid and not expired."""
        return self.otp == otp and self.otp_expiry and timezone.now() <= self.otp_expiry


class PassportData(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="user_details", null=True)
    full_name = models.CharField(max_length=100)
    passport = models.CharField(max_length=9, unique=True)
    birth_date = models.DateField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_time"]

    def __str__(self):
        return f"{self.full_name} ({self.passport})"







