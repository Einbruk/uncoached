from time import sleep
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from users.forms import ExtendedRegister, SurveyFormShort
from .planner import create_plan


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = '/'


class UserLogoutView(LogoutView):
    next_page = '/'


class AccountView(View):
    def get(self, request):
        return render(request, 'users/account.html', {})


def register_view(request):
    if request.method == "POST":
        form = ExtendedRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegister()
    return render(request, 'users/register.html', {'form': form})


class SurveyView(View):
    def get(self, request, year):
        survey_form = SurveyFormShort()
        return render(request, 'users/plan_creation.html', {'form': survey_form})

    def post(self, request, year):
        survey_form = SurveyFormShort(request.POST)
        if survey_form.is_valid():
            create_plan(year, survey_form.cleaned_data, request.user)
        return HttpResponseRedirect('/year/2023/')


class AwaitCreationView(View):
    def get(self, request):
        sleep(3)
        return HttpResponseRedirect('/year/2023/')
