from django.shortcuts import redirect
from django.http import Http404
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from api.serializers import PhotoSerializer
from photo.models import Photo
from album.models import Album


class PhotoUpload(generics.UpdateAPIView):
    queryset = Album.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'photo/photo_upload.html'
    serializer_class = PhotoSerializer

    def get_object(self, pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        photo = Photo.objects.all().filter(album=pk)
        album = Album.objects.all().filter(id=pk)
        serializer = PhotoSerializer(photo, many=True)
        return Response({'serializer': serializer.data, 'image': album})

    def post(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('album_list')
        else:
            return Response(serializer.errors, status=400)
