from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from album import views
from photo.views import PhotoUpload

urlpatterns = [

    url(r'^album/listar/$', views.AlbumList.as_view(), name='album_list'),
    url(r'^album/crear/$', views.AlbumCreate.as_view(), name='album_create'),
    url(r'^album/editar/$', views.AlbumUpdate.as_view(), name='album_update'),
    url(r'^album/eliminar/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album_delete'),
    url(r'^album/(?P<pk>[0-9]+)/image_gallery/$', views.ImageGallery.as_view(), name='image_gallery'),
    url(r'^album/(?P<pk>[0-9]+)/upload_image/$', PhotoUpload.as_view() , name='photo_upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
