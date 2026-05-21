from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    phone_number = forms.CharField(max_length=20, required=False, label='Teléfono')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    pass
