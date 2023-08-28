from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from custom_user.forms import CustomUserProfileForm
from jobs.models import Job

CustomUser = get_user_model()


@login_required
def dashboard_main_view(request):
    job_list = Job.objects.filter(created_by=request.user).order_by('created_on')
    job_paginator = Paginator(job_list, 10)
    context = {
        'job_list': job_list,
    }
    return render(request, 'dashboard/dashboard_home.html', context)


class DashboardMainView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard_home.html'


class DashboardPostedJobsView(LoginRequiredMixin, ListView):
    model = Job
    context_object_name = 'posted_jobs'
    paginate_by = 10
    template_name = 'dashboard/posted_jobs.html'

    def get_queryset(self):
        return Job.objects.filter(created_by=self.request.user).order_by('-created_on')


@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = CustomUserProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect(reverse_lazy('dashboard:update-profile'))
    else:
        form = CustomUserProfileForm(instance=request.user)

    return render(request, 'dashboard/update_profile.html', {'form': form})
