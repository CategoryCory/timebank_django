from django.urls import path

from .views import HomepageView, AboutView, login_success

app_name = 'pages'
urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('login-success/', login_success, name='login_success'),
]