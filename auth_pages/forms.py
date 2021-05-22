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


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=48)
    email = forms.CharField(max_length=64)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    repeat_password = forms.CharField(max_length=64, widget=forms.PasswordInput())

    def clean_repeat_password(self):
        temp_repeat_password = self.cleaned_data['repeat_password']
        temp_password = self.cleaned_data['password']

        userexp = re.compile('^[A-Za-z0-9_-]{8,65}$')

        if len(temp_password) < 8:
            raise ValidationError("Минимальная длина пароля - 8")

        if len(temp_password) > 64:
            raise ValidationError("Максимальная длина пароля - 64")

        if temp_repeat_password != temp_password:
            raise ValidationError("Пароли не совпадают")

        if not userexp.match(temp_password):
            raise ValidationError("В пароле могут присутствовать лишь английские буквы," +
                                  " цифры, дефис и знак подчёркивания")

        return temp_repeat_password

    def clean_login(self):
        temp_login = self.cleaned_data['login']

        userexp = re.compile('^[A-Za-z0-9_-]{3,48}$')

        if len(temp_login) < 3:
            raise ValidationError("Минимальная длина логина - 3")
        elif len(temp_login) > 20:
            raise ValidationError("Максимальная длина логина - 20")

        if not userexp.match(temp_login):
            raise ValidationError("В имени пользователя могут присутствовать лишь английские строчные буквы," +
                                  " цифры, дефис и знак подчёркивания")

        if User.objects.filter(username=temp_login).count() != 0:
            raise ValidationError("Пользователь с таким именем уже зарегистрирован")

        return temp_login

    def clean_email(self):
        temp_email = self.cleaned_data['email']

        if User.objects.filter(email=temp_email).count() != 0:
            raise ValidationError("Пользователь с такой почтой уже зарегистрирован")
        if len(temp_email) > 64:
            raise ValidationError("Максимальная длина почты - 64")
        try:
            validate_email(temp_email)
            valid_email = True
        except ValidationError:
            valid_email = False

        if not valid_email:
            raise ValidationError("В написании адреса почты допущена ошибка")

        return temp_email

    def do_registration(self):
        user = User.objects.create_user(self.cleaned_data['login'], self.cleaned_data['email'],
                                        self.cleaned_data['password'])
        user.save()
        return user
