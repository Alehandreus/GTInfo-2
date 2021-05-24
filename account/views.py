from django.shortcuts import render, loader
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from iu_api.models import TrackedUserObject

# Страница настроек отслеживания
class TrackingSettingsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect("/login")
        tracked_list = request.user.account.tracked_users.all()
        context = {"tracked_list" : tracked_list}
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
        try:
            steam_id = int(request.POST['id'])
        except ValueError:
            return JsonResponse({'status': 'User_id is not a number'}, status=400)
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