from django.db import models
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title