# Generated by Django 4.2 on 2023-04-11 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobcategory',
            options={'verbose_name': 'Job Category', 'verbose_name_plural': 'Job Categories'},
        ),
    ]
