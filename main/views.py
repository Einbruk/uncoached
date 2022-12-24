from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views import View
from datetime import date
# Create your views here.
import os


class LandingView(View):
    def get(self, request):
        path = os.path.abspath(os.path.curdir)
        return render(request, 'main/landing.html', {'path': path})


class MainView(View):
    def get(self, request):
        today = date.today().year
        return HttpResponseRedirect(f'year/{today}/')


class ErrorView(View):
    def get(self, request):
        return render(request, '404.html', {})




