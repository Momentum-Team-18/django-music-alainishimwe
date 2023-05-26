from django.db import models
from django.utils import timezone

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    # artist = models.CharField(max_length=200, blank=True, null=True)
    artist = models.ForeignKey( Musician, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    

    

# class Visitor(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name
    
# class Favorite(models.Model):
#     visitor = models.ForeignKey(to='Visitor', on_delete=models.CASCADE)
#     album = models.ForeignKey(to='Album', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.visitor


