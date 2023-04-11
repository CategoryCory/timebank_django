from django.contrib import admin

from .models import Job, JobCategory, JobSchedule


class JobScheduleInline(admin.TabularInline):
    model = JobSchedule
    extra = 0


class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug', )
    list_per_page = 25
    prepopulated_fields = {'category_slug': ('category_name', )}


class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'created_by', 'job_status', 'expires_on', )
    list_editable = ('job_status', )
    list_per_page = 25
    search_fields = ('job_name', 'job_category', 'job_status', )
    inlines = [
        JobScheduleInline
    ]


admin.site.register(JobCategory, JobCategoryAdmin)
admin.site.register(Job, JobAdmin)
