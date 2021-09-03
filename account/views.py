from django.shortcuts import render, loader
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from iu_api.models import TrackedUserObject
from .forms import *
import requests
from bs4 import BeautifulSoup


# Страница настроек отслеживания
class TrackingSettingsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        tracked_list = request.user.account.tracked_users.all()
        context = {"tracked_list": tracked_list}
        template = loader.get_template("account/tracking_settings.html")
        return HttpResponse(template.render(context, request))


class DeleteTrackedUser(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        try:
            steam_id = int(request.POST['id'])
        except ValueError:
            return JsonResponse({'status': 'User_id is not a number'})
        if request.user.account.tracked_users.get(steam_id=steam_id) is None:
            return JsonResponse({'status': 'UserNotFound'})
        tracked_user = request.user.account.tracked_users.filter(steam_id=steam_id).first()
        request.user.account.tracked_users.remove(tracked_user)
        return JsonResponse({'status': 'ok'})


class AddTrackedUser(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")

        steam_id = request.POST['id']
        url = f"https://steamcommunity.com/profiles/{steam_id}/"
        response = requests.get(url)
        if response.status_code != 200:
            return JsonResponse({'status': 'UnknownError'}, status=400)
        soup = BeautifulSoup(response.content, 'html.parser')

        name_elem = soup.find("span", class_="actual_persona_name")
        if name_elem is None:
            return JsonResponse({'status': 'InvalidID'}, status=400)

        recent_activity_elem = soup.find("div", class_="profile_recentgame_header")
        if recent_activity_elem is None:
            return JsonResponse({'status': 'PrivateProfile'}, status=400)

        try:
            tracked_user = request.user.account.tracked_users.get(steam_id=steam_id)
        except TrackedUserObject.DoesNotExist:
            tracked_user = None

        if request.user.account.tracked_users.count() >= 10:
            return JsonResponse({'status': 'TooManyUsers'}, status=400)

        if tracked_user is None:
            try:
                tracked_user = TrackedUserObject.objects.get(steam_id=steam_id)
            except TrackedUserObject.DoesNotExist:
                tracked_user = None
            if tracked_user is None:
                tracked_user = TrackedUserObject.objects.create(steam_id=steam_id)
            else:
                tracked_user = TrackedUserObject.objects.get(steam_id=steam_id)
            request.user.account.tracked_users.add(tracked_user)
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'UserAlreadyAdded'}, status=400)


class MainSettingsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        context = {}
        template = loader.get_template("account/main_settings.html")
        return HttpResponse(template.render(context, request))

    def post(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        context = {}
        template = loader.get_template("account/main_settings.html")
        current_form = ChangePasswordForm(request.POST)
        if current_form.is_valid():
            result = current_form.change_password(request.user, request)
            if not result:
                context["change_error"] = True
                return HttpResponse(template.render(context, request))
            context["change_success"] = True
            return HttpResponse(template.render(context, request))
        else:
            context["form"] = current_form
            return HttpResponse(template.render(context, request))