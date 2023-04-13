from django.urls import path

from .views import ContactUsView

app_name = 'contacts'
urlpatterns = [
    path('', ContactUsView.as_view(), name='contact-us'),
]
