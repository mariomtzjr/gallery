from django.contrib import admin
from photo.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'album', 'uploaded_at',)
