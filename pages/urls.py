from django.urls import path

from .views import HomepageView, AboutView, TermsConditionsView, PrivacyPolicyView, login_success

app_name = 'pages'
urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('terms/', TermsConditionsView.as_view(), name='terms'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy'),
    path('login-success/', login_success, name='login_success'),
]