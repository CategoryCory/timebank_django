from django import forms

from .models import Contact


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('contact_name', 'contact_email', 'contact_message', )
        widgets = {
            'contact_message': forms.Textarea(attrs={'rows': 4, }),
        }
        labels = {
            'contact_name': 'Your name',
            'contact_email': 'Your email address',
            'contact_message': 'What is your message or question?',
        }
