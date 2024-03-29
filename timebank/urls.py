from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('contact/', include('contact.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('pages.urls')),
    re_path(r'^tinymce/', include('tinymce.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
