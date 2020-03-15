from django.db import models


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='gallery', default='gallery/no-img.jpg')
    caption = models.CharField(max_length=100)
    album = models.ForeignKey('album.Album', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
