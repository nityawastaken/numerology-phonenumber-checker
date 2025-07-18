from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, timedelta

# Create your models here.

def payment_screenshot_path(instance, filename):
    return f'payments/user_{instance.id}/{filename}'

class CustomUser(AbstractUser):
    # has_access = models.BooleanField(default=False)  # You can later check this
    subscription_start = models.DateField(null=True, blank=True)
    subscription_duration_days = models.IntegerField(null=True, blank=True)
    payment_screenshot = models.ImageField(upload_to=payment_screenshot_path, null=True, blank=True)

    @property
    def has_access(self):
        if self.subscription_start and self.subscription_duration_days:
            end_date = self.subscription_start + timedelta(days=self.subscription_duration_days)
            return date.today() <= end_date
        return False
    
    @property
    def access_end_date(self):
        if self.subscription_start and self.subscription_duration_days:
            return self.subscription_start + timedelta(days=self.subscription_duration_days)
        return None