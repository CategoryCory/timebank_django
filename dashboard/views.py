from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

from custom_user.forms import CustomUserProfileForm, UploadProfileImageForm
from jobs.models import Job
from custom_user.models import CustomUserProfileImage

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


@login_required
def update_profile_image(request):
    if request.method == 'POST':
        form = UploadProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get('profile_image')
            # TODO: Check if profile photo exists and update if so
            if hasattr(request.user, 'profile_image'):
                current_photo = request.user.profile_image
                current_photo.profile_image = img
                current_photo.save()
            else:
                profile_photo = CustomUserProfileImage.objects.create(
                    user=request.user,
                    profile_image=img,
                )
                profile_photo.save()
            return redirect(reverse_lazy('dashboard:update-profile-image'))
    else:
        form = UploadProfileImageForm()
    return render(request, 'dashboard/update_profile_image.html', {'form': form})
