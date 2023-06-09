# Generated by Django 4.2 on 2023-04-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.PositiveSmallIntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1, help_text='The day of the week for this time slot', max_length=16)),
                ('time_begin', models.TimeField(help_text='The beginning time for this time slot')),
                ('time_end', models.TimeField(help_text='The ending time for this time slot')),
                ('job_schedule_status', models.CharField(choices=[('open', 'Open'), ('filled', 'Filled')], default='open', help_text='The current status of this time slot', max_length=16)),
            ],
        ),
    ]
