# Generated by Django 4.2.4 on 2023-09-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_faqentry_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqentry',
            name='display_order',
            field=models.PositiveIntegerField(help_text='The order in which this entry should be displayed', unique=True),
        ),
    ]
