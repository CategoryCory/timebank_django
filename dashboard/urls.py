from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.DashboardMainView.as_view(), name='dashboard-home'),
    path('posted-jobs/', views.DashboardPostedJobsView.as_view(), name='posted-jobs'),
    path('update-profile/', views.update_profile_view, name='update-profile'),
    path('update-profile-image/', views.update_profile_image, name='update-profile-image'),
]
