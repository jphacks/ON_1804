from django.db import models

class TrainingMenu(models.Model):
    TIMES = 0
    SECOND = 1
    MINUTES = 2

    training_name = models.CharField(max_length=50)
    times_number = models.IntegerField(default=0)
    sets_number = models.IntegerField(default=0)
    times_type = models.IntegerField(default=50) #回数，秒，分
    week = models.IntegerField(default=0) #SUN=0, MON=1...
