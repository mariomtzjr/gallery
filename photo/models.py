from django.db import models
from album.models import Album


# Create your models here.
class Photo(models.Model):
    url = ""
    caption = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
