from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from datetime import date

class LandingView(View):
    def get(self, request):
        return render(request, 'main/landing.html', {})


class MainView(View):
    def get(self, request):
        today = date.today().year
        return HttpResponseRedirect(f'year/{today}/')


class ErrorView(View):
    def get(self, request):
        return render(request, '404.html', {})




