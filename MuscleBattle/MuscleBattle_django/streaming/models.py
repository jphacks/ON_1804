from django.db import models

class Room(models.Model):
    room_hash = models.CharField(max_length=100, unique=True)
