from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('btc','deposit',)
        widgets = {'btc': forms.HiddenInput(), 'deposit': forms.HiddenInput()}