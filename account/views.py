from django.shortcuts import render, loader
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse


# Страница настроек отслеживания
class TrackingSettingsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        context = {}
        template = loader.get_template("account/tracking_settings.html")
        return HttpResponse(template.render(context, request))