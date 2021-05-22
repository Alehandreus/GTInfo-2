from django.urls import path
from .views import *

urlpatterns = [
    path('visualisation/', VisualisationView.as_view()),
]