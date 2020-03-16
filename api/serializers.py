from rest_framework import serializers
from album.models import Album
from photo.models import Photo


class AlbumCreateSerializer(serializers.ModelSerializer):
    """ AlbumCreateSerializer
    Descripción:
    Clase que convierte la información al estandar de comunicación JSON.
    """
    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at',)


class AlbumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

        read_only_fields = ('created_at', 'updated_at',)


class PhotoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        Create and return a new 'Photo' instance, given the validated data.
        """
        return Photo.objects.create(**validated_data)

    class Meta:
        model = Photo
        fields = ('image', 'caption', 'album')
