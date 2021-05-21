from django.shortcuts import render
from django.template import loader
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login
from .forms import LoginForm


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            context = {}
            template = loader.get_template("auth_pages/login.html")
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect("/")

    def post(self, request):
        if not request.user.is_authenticated:
            current_form = LoginForm(request.POST)

            if current_form.is_valid():
                user = current_form.do_auth()
                if user is not None:
                    login(request, user)
                    remember_me = current_form.cleaned_data.get("remember_me_option", None)
                    if remember_me is None or remember_me != "on":
                        request.session.set_expiry(0)
                    return HttpResponseRedirect("/")
                else:
                    template = loader.get_template('auth_pages/login.html')
                    return HttpResponse(template.render({'form': current_form}, request))
            else:
                template = loader.get_template('auth_pages/login.html')
                return HttpResponse(template.render({'form': current_form}, request))
        else:
            return HttpResponseRedirect("/")


class RegisterView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            context = {}
            template = loader.get_template("auth_pages/register.html")
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect("/")


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
