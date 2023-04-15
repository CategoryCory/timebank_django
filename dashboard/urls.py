from django.urls import path

from .views import dashboard_main_view, update_profile_view

app_name = 'dashboard'
urlpatterns = [
    path('', dashboard_main_view, name='dashboard-home'),
    path('update-profile/', update_profile_view, name='update-profile'),
]
