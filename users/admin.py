# admin.py
from django.contrib import admin
from .models import Account, PassportData


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'is_active', 'is_staff', 'created_time']
    search_fields = ['phone_number', 'is_active']
    list_filter = ['is_active', 'is_staff']

@admin.register(PassportData)
class PdataAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'passport', 'birth_date', 'created_time']
    search_fields = ['full_name', 'passport']
    list_filter = ['birth_date']
