from django.urls import path
from planner import views

urlpatterns = [
    path('year/<int:year>/', views.YearView.as_view(), name='year'),
    path('year/<int:year>/week/<int:week>/', views.WeekView.as_view(), name='week'),
]


