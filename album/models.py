from django.db import models
from photo.models import Photo


# Create your models here.
class Album(models.Model):
    COVER_CHOICES = (
            ('SOFT COVER', 'SOFT COVER'),
            ('HARD COVER', 'HARD COVER'),
    )
    title = models.CharField(max_length=100)
    cover = models.CharField(
        max_length=20,
        choices=COVER_CHOICES,
        default='SOFT COVER',
    )
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
