from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    street_address = models.CharField(max_length=100)
    street_address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=25)
    birthday = models.DateField(default=timezone.now)
    biography = models.TextField()
    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    linkedin = models.CharField(max_length=250, blank=True)
    is_approved = models.BooleanField(default=False,
                                      help_text='Indicates whether this user has been approved to use this site')

    @property
    def user_initials(self) -> str:
        if self.first_name and self.last_name:
            return f'{self.first_name[:1]}{self.last_name[:1]}'
        else:
            return f'{self.username[:1]}'

    @property
    def current_profile_image(self) -> str:
        if not hasattr(self, 'profile_image'):
            return f'https://ui-avatars.com/api/?name={self.user_initials}&color=4338CA&background=C7D2FE'
        else:
            return self.profile_image.profile_image.url

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username


class CustomUserProfileImage(models.Model):
    profile_image = models.ImageField(upload_to='profile_images')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile_image')

    class Meta:
        verbose_name = 'Profile Image'
        verbose_name_plural = 'Profile Images'
