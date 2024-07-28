from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' نام خود را وارد کنید'}),
        label='',
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' نام خانوادگی خود را وارد کنید'}),
        label='',
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' ایمیل خود را وارد کنید'}),
        label='',
    )
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' نام کاربری'}),
        label='',
    )
    password1 = forms.CharField(
        label='',
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': ' رمز بالای 8 کارکتر را وارد کنید'
            }
        )
    )

    password2 = forms.CharField(
        label='',
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'name': 'password',
                'type': 'password',
                'placeholder': ' دوباره رمز خود را وارد کنید'
            }
        )
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')