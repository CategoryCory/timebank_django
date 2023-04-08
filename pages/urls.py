from django.urls import path

from .views import homepage_view, login_success

app_name = 'pages'
urlpatterns = [
    path('', homepage_view, name='home'),
    path('login-success/', login_success, name='login_success'),
]