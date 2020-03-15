from django.db import models
from photo.models import Photo


# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    photos = models.ManyToManyField(Photo, related_name='+')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
