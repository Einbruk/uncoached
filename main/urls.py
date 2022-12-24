from django.urls import path
from main import views

urlpatterns = [
    path('landing/', views.LandingView.as_view(), name='landing-page'),
    path('', views.MainView.as_view(), name='main-page'),
    path('404/', views.ErrorView.as_view()),
]
