# Generated by Django 4.2.4 on 2023-09-02 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_faqentry_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='faqentry',
            name='display_order',
            field=models.PositiveIntegerField(default=1, help_text='The order in which this entry should be displayed'),
            preserve_default=False,
        ),
    ]
