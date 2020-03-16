from django.contrib import admin
from album.models import Album
from photo.models import Photo


# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]
    list_display = ('title', 'created_at',)
