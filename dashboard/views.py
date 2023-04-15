from django.shortcuts import render


def dashboard_main_view(request):
    return render(request, 'dashboard/dashboard_home.html')


def update_profile_view(request):
    return render(request, 'dashboard/update_profile.html')
