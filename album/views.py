from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from api.serializers import AlbumCreateSerializer, AlbumListSerializer
from album.models import Album


# Create your views here.
class AlbumList(generics.ListAPIView):
    """Clase InmubleList
    Descripción
    Lista todas los albumes que se encuentran en venta.
    Restricciones:
        Ninguna.
    """
    queryset = Album.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'album/album_listar.html'
    serializer_class = AlbumListSerializer

    def get(self, request, *args, **kwargs):
        queryset = Album.objects.all()
        serializer = AlbumListSerializer(queryset, many=True)
        return Response({'albumes': serializer.data})
