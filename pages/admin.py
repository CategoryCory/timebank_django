from django.contrib import admin
from .models import FAQEntry


class FAQEntryAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('title', 'display_order', 'created_on', 'last_modified', )
    list_editable = ('display_order', )


admin.site.register(FAQEntry, FAQEntryAdmin)
