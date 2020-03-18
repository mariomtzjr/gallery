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

    def get_object(self, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk', None)
            return pk
        except Album.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = self.get_object()
        photo = Photo.objects.all().filter(album=pk)
        album = Album.objects.all().filter(id=pk)
        serializer = PhotoSerializer(photo, many=True)
        return Response({'serializer': serializer.data, 'image': album, 'pk': pk})

    def post(self, request, *args, **kwargs):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('image_gallery')
        else:
            return Response(serializer.errors, status=400)
