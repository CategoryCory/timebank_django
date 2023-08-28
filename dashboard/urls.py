from django.urls import path

from .views import DashboardMainView, DashboardPostedJobsView, update_profile_view

app_name = 'dashboard'
urlpatterns = [
    path('', DashboardMainView.as_view(), name='dashboard-home'),
    path('posted-jobs/', DashboardPostedJobsView.as_view(), name='posted-jobs'),
    path('update-profile/', update_profile_view, name='update-profile'),
]
