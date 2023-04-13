from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email', 'contact_timestamp', )
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
