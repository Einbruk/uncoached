from django.urls import path
from main import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('landing/', cache_page(30)(views.LandingView.as_view()), name='landing-page'),
    path('', views.MainView.as_view(), name='main-page'),
    path('404/', views.ErrorView.as_view()),
]
