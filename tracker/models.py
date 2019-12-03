from django.db import models

# Create your models here.

class Squirrel(models.Model):
    latitude = models.FloatField(blank=False)
    longitude = models.FloatField(blank=True)
    unique_squirrel_id = models.CharField(max_length=14)
    shift = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    age = models.CharField(max_length = 200, blank=True)
    primary_fur_color = models.CharField(max_length = 200, blank=True)
    location = models.CharField(max_length = 200)
    specific_location = models.CharField(max_length = 200)
    running = models.BooleanField(blank=True)
    chasing = models.BooleanField(blank=True)
    climbing = models.BooleanField(blank=True)
    eating = models.BooleanField(blank=True)
    foraging = models.BooleanField(blank=True)
    other_activities = models.CharField(max_length = 200)
    kuks = models.BooleanField(blank=True)
    quaas = models.BooleanField(blank=True)
    moans = models.BooleanField(blank=True)
    tail_flags = models.BooleanField(blank=True)
    tail_twitches = models.BooleanField(blank=True)
    approaches = models.BooleanField(blank=True)
    indifferent = models.BooleanField(blank=True)
    runs_from = models.BooleanField(blank=True)
