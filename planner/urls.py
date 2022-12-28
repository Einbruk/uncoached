from django.urls import path
from planner import views

urlpatterns = [
    path('year/<int:year>/', views.YearView.as_view(), name='year'),
    path('year/<int:year>/week/<int:week>/', views.WeekView.as_view(), name='week'),
    path('year/<int:year>/week/<int:week>/edit/', views.WeekEditView.as_view(), name='edit week'),
    path('year/<int:year>/week/<int:week>/add-<int:day>-<int:month>/',
         views.WorkoutCreateView.as_view(), name='create-wo'),
    path('year/<int:year>/week/<int:week>/<int:id>/', views.WorkoutView.as_view(), name='workout view'),
    path('year/<int:year>/week/<int:week>/<int:id>/workout_del/',
         views.WorkoutDeleteView.as_view(), name='workout delete'),
    path('year/<int:year>/week/<int:week>/<int:id>/edit/', views.WorkoutEditView.as_view(), name='workout edit'),
]


