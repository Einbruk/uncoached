from django.urls import path
from users import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('login/', cache_page(30)(views.UserLoginView.as_view()), name='login'),
    path('logout/', cache_page(30)(views.UserLogoutView.as_view()), name='logout'),
    path('register/', views.register_view, name='register'),
    path('new_plan_<int:year>/', views.SurveyView.as_view(), name='create'),
    path('new_plan/await/', views.AwaitCreationView.as_view(), name='await'),
    path('account/', cache_page(30)(views.AccountView.as_view()), name='account'),
    # path('edit_account/', views.EditAccView.as_view(), name='edit_account'),
]
