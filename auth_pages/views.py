from django.shortcuts import render
from django.template import loader
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect


class LoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            context = {}
            template = loader.get_template("auth_pages/login.html")
            return HttpResponse(template.render(context, request))
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