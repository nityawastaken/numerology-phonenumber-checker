from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['payment_screenshot', 'subscription_duration_days']
class PaymentForm(forms.Form):
    payment_screenshot = forms.ImageField(required=True)
    duration = forms.ChoiceField(choices=[('1', '1 Day'), ('7', '7 Days'), ('30', '30 Days')], required=True)