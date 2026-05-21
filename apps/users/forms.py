from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

_DARK_INPUT = 'form-control bg-dark text-light border-secondary'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    phone_number = forms.CharField(max_length=20, required=False, label='Teléfono')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': _DARK_INPUT})


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': _DARK_INPUT})
