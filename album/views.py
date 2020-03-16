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


class AlbumCreate(generics.CreateAPIView):
    """Clase AlbumCreate
    Descripción:
    Vista que renderiza un formulario personalizado para realizar
    la creación/registro de un album.
    Métodos:
    - get: Realiza una consulta de los métodos que se encuentran creados
    y los devuelve.
    - post: Realiza el envío de datos a la api(/album/crear)
    """
    queryset = Album.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'album/album_crear.html'
    serializer_class = AlbumCreateSerializer

    def get(self, request, *args, **kwargs):
        queryset = Album.objects.all()
        serializer = AlbumCreateSerializer(queryset, many=True)
        return Response({'albumes': serializer.data})

    def post(self, request):
        serializer = AlbumListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('album_list')
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumUpdate(generics.UpdateAPIView):
    """Clase AlbumUpdate
    Descripción
    Permite modificar los valores de los campos por los que está conformado
    el modelo Album.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'album/album_update.html'

    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumListSerializer(album)
        return Response({'serializer': serializer, 'album': album})

    def post(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumListSerializer(album, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'album': album})
        serializer.save()
        return redirect('album_list')
