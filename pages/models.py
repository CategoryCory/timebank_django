from django.db import models
from tinymce.models import HTMLField


class FAQEntry(models.Model):
    title = models.CharField(max_length=250, help_text='The title for this FAQ entry')
    body = HTMLField(help_text='The response to this question')
    display_order = models.PositiveIntegerField(unique=True,
                                                help_text='The order in which this entry should be displayed')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ Entry'
        verbose_name_plural = 'FAQ Entries'

    def __str__(self) -> str:
        return self.title
