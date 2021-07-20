from django.shortcuts import render, loader
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse


class VisualisationView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        context = {}
        template = loader.get_template("visualisation/main.html")
        return HttpResponse(template.render(context, request))


class HoursView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        context = {}
        template = loader.get_template("visualisation/hours.html")
        return HttpResponse(template.render(context, request))