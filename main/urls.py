from django.urls import path
from main import views

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing-page'),
]