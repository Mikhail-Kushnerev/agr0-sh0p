from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from dataclasses import field
from pyexpat import model
from django import forms


from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class LoginForm(forms.Form):
    username = forms.CharField()
    # email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)


# class UserChangeForm(UserChangeForm):
#     class Meta:
#         model = User