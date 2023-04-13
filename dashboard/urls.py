from django.urls import path

from .views import update_profile_view

app_name = 'dashboard'
urlpatterns = [
    path('profile/', update_profile_view, name='profile'),
]
