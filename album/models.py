from django.db import models
from photo.models import Photo


# Create your models here.
class Album(models.Model):
    COVER_CHOICES = (
            ('SC', 'SOFT COVER'),
            ('HC', 'HARD COVER'),
    )
    title = models.CharField(max_length=100)
    cover = models.CharField(
        max_length=20,
        choices=COVER_CHOICES,
        default='SOFT COVER',
    )
    photos = models.ManyToManyField(Photo, related_name='+', blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
