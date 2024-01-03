from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

CustomUser = get_user_model()


class JobCategory(models.Model):
    category_name = models.CharField(max_length=150)
    category_slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'Job Category'
        verbose_name_plural = 'Job Categories'

    def __str__(self) -> str:
        return self.category_name


class Job(models.Model):
    OPEN = 'open'
    CUSTOM = 'custom'

    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    COMPLETED = 'completed'
    DELETED = 'deleted'

    JOB_SCHEDULE_CHOICES = [
        (OPEN, 'Open'),
        (CUSTOM, 'Custom'),
    ]

    JOB_STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable'),
        (COMPLETED, 'Completed'),
        (DELETED, 'Deleted'),
    ]

    job_name = models.CharField(max_length=100, help_text='A brief name for this job')
    job_description = models.TextField(help_text='A description of the work related to this job')
    expires_on = models.DateField(help_text='When does this job expire?')
    job_schedule_type = models.CharField(max_length=25,
                                         choices=JOB_SCHEDULE_CHOICES,
                                         default=OPEN,
                                         help_text='Indicates whether this job can be done anytime, or by schedule')
    job_status = models.CharField(max_length=25,
                                  choices=JOB_STATUS_CHOICES,
                                  default=AVAILABLE,
                                  help_text='Indicates the current status of this job')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    job_category = models.ForeignKey(JobCategory, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.job_name

    # TODO: Add get_absolute_url


class JobSchedule(models.Model):
    OPEN = 'open'
    FILLED = 'filled'

    SUN = 0
    MON = 1
    TUES = 2
    WED = 3
    THURS = 4
    FRI = 5
    SAT = 6

    JOB_SCHEDULE_STATUS = [
        (OPEN, 'Open'),
        (FILLED, 'Filled'),
    ]

    DAY_OF_WEEK = [
        (SUN, 'Sunday'),
        (MON, 'Monday'),
        (TUES, 'Tuesday'),
        (WED, 'Wednesday'),
        (THURS, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'),
    ]

    day_of_week = models.PositiveSmallIntegerField(choices=DAY_OF_WEEK,
                                                   default=MON,
                                                   help_text='The day of the week for this time slot')
    time_begin = models.TimeField(help_text='The beginning time for this time slot')
    time_end = models.TimeField(help_text='The ending time for this time slot')
    job_schedule_status = models.CharField(max_length=16,
                                           choices=JOB_SCHEDULE_STATUS,
                                           default=OPEN,
                                           help_text='The current status of this time slot')
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.day_of_week}, {self.time_begin} - {self.time_end}'
