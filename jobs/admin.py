from django.contrib import admin

from .models import JobCategory


class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug', )
    list_per_page = 25
    prepopulated_fields = {'category_slug': ('category_name', )}


admin.site.register(JobCategory, JobCategoryAdmin)
