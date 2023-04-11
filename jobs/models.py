from django.db import models
from django.urls import reverse


class JobCategory(models.Model):
    category_name = models.CharField(max_length=150)
    category_slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'

    def __str__(self):
        return self.category_name
