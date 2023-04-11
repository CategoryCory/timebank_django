from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


@login_required
def login_success(request):
    if request.user.is_approved is True:
        # TODO: This needs to be replaced with a redirect to the user dashboard once created
        return redirect('pages:home')
    else:
        return redirect('pages:home')


class HomepageView(TemplateView):
    template_name = 'pages/home.html'


class AboutView(TemplateView):
    template_name = 'pages/about.html'
