from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(CustomUser)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Subscription Info", {
            "fields": ("subscription_start", "subscription_duration_days", "payment_screenshot"),
        }),
    )