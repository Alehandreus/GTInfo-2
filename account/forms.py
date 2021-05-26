from django import forms
from django.core.exceptions import ValidationError
import re
from django.contrib.auth import authenticate, login


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    password_repeat = forms.CharField(max_length=64, widget=forms.PasswordInput())

    def clean_password_repeat(self):
        temp_password_repeat = self.cleaned_data['password_repeat']
        temp_password = self.cleaned_data['password']
        temp_old_password = self.cleaned_data['old_password']

        userexp = re.compile('^[A-Za-z0-9_-]{8,100}$')

        if len(temp_password) < 8:
            raise ValidationError("Минимальная длина пароля - 8.")

        if len(temp_password) > 100:
            raise ValidationError("Максимальная длина пароля - 100.")

        if temp_password != temp_password_repeat:
            raise ValidationError("Пароли не совпадают.")

        if not userexp.match(temp_password):
            raise ValidationError("В пароле могут присутствовать лишь английские буквы,"+
                                  " цифры, дефис и знак подчёркивания")

        if temp_old_password == temp_password:
            raise ValidationError('Старый пароль совпадает с новым')

        return temp_password

    def change_password(self, user, request):
        check_user = authenticate(username=user.username, password=self.cleaned_data['old_password'])
        if check_user is not None:
            user.set_password(self.cleaned_data['password'])
            user.save()
            user = authenticate(username=user.username, password=self.cleaned_data['password'])
            login(request, user)
            return True
        else:
            return False
