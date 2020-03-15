from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from album import views

urlpatterns = [

    url(r'^album/listar/$', views.AlbumList.as_view(), name='album_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
