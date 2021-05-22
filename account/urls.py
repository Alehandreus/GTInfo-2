from django.urls import path
from .views import *

urlpatterns = [
    path('tracking_settings/', TrackingSettingsView.as_view()),
]