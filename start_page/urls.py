from .views import StartPageView
from django.urls import path


urlpatterns = [
    path('', StartPageView.as_view()),
]