from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from album import views

urlpatterns = [

    url(r'^album/listar/$', views.AlbumList.as_view(), name='album_list'),
    url(r'^album/crear/$', views.AlbumCreate.as_view(), name='album_create'),
    url(r'^album/editar/$', views.AlbumUpdate.as_view(), name='album_update'),
    url(r'^album/eliminar/(?P<pk>[0-9]+)/$', views.AlbumDelete.as_view(), name='album_delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
