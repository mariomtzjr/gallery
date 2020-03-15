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
        fields = (
            'title',
            'photos',
        )

        read_only_fields = ('created_at', 'updated_at',)


class AlbumUpdateSerializer(serializers.ModelSerializer):
    pass


class AlbumDeleteSerializer(serializers.ModelSerializer):
    pass