from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'passport']
    search_fields = ['full_name', 'phone_number', 'passport']
    list_filter = ['full_name', 'phone_number', 'passport']