from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .models import FAQEntry


@login_required
def login_success(request):
    if not request.user.is_approved:
        return redirect(reverse_lazy('dashboard:update-profile'))
    else:
        return redirect(reverse_lazy('dashboard:dashboard-home'))


class HomepageView(TemplateView):
    template_name = 'pages/home.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        faq_list = FAQEntry.objects.order_by('display_order')
        context.update({'faq_list': faq_list})
        return context


class TermsConditionsView(TemplateView):
    template_name = 'pages/terms.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'pages/privacy.html'
