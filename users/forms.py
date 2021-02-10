from users.models import profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    category = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'category', 'password1', 'password2', ]


class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = profile
        fields = ['image']
