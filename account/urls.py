from django.urls import path
from .views import *

urlpatterns = [
    path('main_settings/', MainSettingsView.as_view()),
    path('tracking_settings/', TrackingSettingsView.as_view()),
    path('tracking_settings_delete_user/', DeleteTrackedUser.as_view()),
    path('tracking_settings_add_user/', AddTrackedUser.as_view())
]