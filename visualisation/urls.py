from django.urls import path
from .views import *

urlpatterns = [
    path('visualisation/', VisualisationView.as_view()),
    path('visualisation/hours/', HoursView.as_view()),
    path('get_tracked/', GetTrackedUsersView.as_view()),
]