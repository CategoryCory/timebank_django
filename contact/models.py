from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_message = models.TextField()
    contact_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.contact_name} - {self.contact_timestamp}'
