# Generated by Django 4.2.5 on 2023-09-04 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0007_remove_customuser_profile_image_url_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuserprofileimage',
            options={'verbose_name': 'Profile Image', 'verbose_name_plural': 'Profile Images'},
        ),
        migrations.RemoveField(
            model_name='customuserprofileimage',
            name='original_filename',
        ),
    ]
