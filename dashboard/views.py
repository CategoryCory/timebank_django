from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from custom_user.forms import CustomUserProfileForm

CustomUser = get_user_model()


def dashboard_main_view(request):
    return render(request, 'dashboard/dashboard_home.html')


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
