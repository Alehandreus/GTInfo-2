from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.validators import validate_email
import re


class LoginForm(forms.Form):
    login = forms.CharField(max_length=32)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    remember_me_option = forms.CharField(max_length=16, required=False)

    def clean_password(self):
        temp_login = self.cleaned_data['login'].lower()
        temp_password = self.cleaned_data['password']

        user = authenticate(username=temp_login, password=temp_password)

        if user is None:
            raise ValidationError("Комбинация логина и пароля не подошла.")

        return temp_password

    def do_auth(self):
        user = authenticate(username=self.cleaned_data['login'], password=self.cleaned_data['password'])
        return user
