from django.shortcuts import render
from django.views import View
# Create your views here.
import os


class LandingView(View):
    def get(self, request):
        path = os.path.abspath(os.path.curdir)
        return render(request, 'main/landing.html', {'path': path})



