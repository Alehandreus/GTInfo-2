from django.shortcuts import render, loader
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

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


class GetTrackedUsersView(View):
    def post(self, request):
        context = {}
        if not request.user.is_authenticated:
            context["status"] = "unauthorized"
        else:
            try:
                context["users"] = [user.steam_id for user in request.user.account.tracked_users.all()]
                print(context)
                context["status"] = "ok"
            except:
                context["status"] = "error"
        return JsonResponse(context)