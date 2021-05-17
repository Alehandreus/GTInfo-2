from django.shortcuts import render
from django.views import View
from django.template import loader
from django.http import HttpResponse


# Create your views here.
class StartPageView(View):
    def get(self, request):
        template = loader.get_template("start_page/main.html")
        context = dict()
        return HttpResponse(template.render(context, request))