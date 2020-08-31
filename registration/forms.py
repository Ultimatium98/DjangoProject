from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('ip',)
        widgets = {'ip': forms.HiddenInput()}
