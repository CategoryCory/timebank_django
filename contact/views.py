from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactUsForm
from .models import Contact


class ContactUsView(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'contact/contact-us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('contacts:contact-us')
    success_message = 'Your message has been sent!'
