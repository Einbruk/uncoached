from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=40, blank=True, null=True, unique=True)
    email = models.EmailField('email address', unique=True, default=None)
    phone = models.CharField(max_length=15, default=None, null=True, blank=True)
    tg_id = models.IntegerField(default=0, null=True, blank=True)
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return "{}".format(self.username)


class Year(models.Model):
    year = models.IntegerField()
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    goals = models.TextField(max_length=300)
    objectives = models.TextField(max_length=300)
    hrs_planned = models.IntegerField()

    def __str__(self):
        return '{}, {}'.format(self.athlete.username, self.year)


class Week(models.Model):
    week_no = models.IntegerField()
    starts_with = models.DateField()
    hrs_planned = models.FloatField()
    period = models.CharField(max_length=10)
    hrs_fact = models.FloatField(default=0, blank=True, null=True)
    km_fact = models.IntegerField(default=0, blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    comment = models.CharField(max_length=80, default='', blank=True, null=True)
    race = models.CharField(max_length=40, default='', blank=True, null=True)
    priority = models.CharField(max_length=1, default='', blank=True, null=True)

    class Meta:
        db_table = 'week'
        ordering = ['week_no']

    def __str__(self):
        return '{}, {}-{}'.format(self.year.athlete.username, self.year.year, self.week_no)


class Day(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    day = models.DateField()
    week_day = models.CharField(max_length=8)

    def __str__(self):
        return '{}, {}-{}'.format(self.week.year.athlete.username, self.week.year.year, self.day)


class Workout(models.Model):
    title = models.CharField(max_length=40, default='Workout')
    type = models.CharField(max_length=10, default='Workout')
    task = models.TextField(max_length=400)
    feelings = models.TextField(max_length=400, default='-', null=True, blank=True)
    duration_min = models.IntegerField()
    distance = models.FloatField(default=0)
    alt_gain = models.IntegerField(default=0)
    started_at = models.DateTimeField(default=None, null=True, blank=True)
    pe = models.IntegerField(default=None, null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '{}, {}-{}-{}'.format(self.week.year.athlete.username, self.week.year.year, self.week.week_no, self.day)

