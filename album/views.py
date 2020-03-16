from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from api.serializers import AlbumCreateSerializer, AlbumListSerializer, PhotoSerializer
from album.models import Album
from photo.models import Photo


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


class AlbumDelete(generics.RetrieveUpdateDestroyAPIView):
    """Clase AlbumDelete
    Descripción
    Permite eliminar los registros (albumes) que se encuentran almacenados.
    Métodos:
        - get: Obtiene los objetos (albumes listadas)
        - post: Envía la petición a la api (ruta album/eliminar) para
        eliminar el album. Se pasa como argumento el id del registro
        que pertenece al album.
    """
    queryset = Album.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'album/album_eliminar.html'

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        album = self.get_object(pk)
        serializer = AlbumListSerializer(album)
        return Response({'serializer': serializer, 'album': album})

    def post(self, request, pk):
        album = self.get_object(pk)
        album.delete()
        return redirect('album_list')


class ImageGallery(generics.ListAPIView):

    queryset = Album.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'album/image_gallery.html'

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # album = self.get_object(pk)
        photos = Photo.objects.all().filter(album=pk)
        print(photos)
        serializer = PhotoSerializer(photos)
        return Response({'serializer': serializer, 'images': photos})
