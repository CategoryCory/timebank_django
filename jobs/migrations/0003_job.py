# Generated by Django 4.2 on 2023-04-11 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_alter_jobcategory_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(help_text='A brief name for this job', max_length=100)),
                ('job_description', models.TextField(help_text='A description of the work related to this job')),
                ('expires_on', models.DateField(help_text='When does this job expire?')),
                ('job_schedule_type', models.CharField(choices=[('open', 'Open'), ('custom', 'Custom')], default='open', help_text='Indicates whether this job can be done anytime, or by schedule', max_length=25)),
                ('job_status', models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable'), ('completed', 'Completed'), ('deleted', 'Deleted')], default='available', help_text='Indicates the current status of this job', max_length=25)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('job_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.jobcategory')),
            ],
        ),
    ]
