from rest_framework import serializers
from .models import Serie, Movie, Media

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie 
        fields = "__all__"

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie 
        fields = "__all__"

class MediaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    machine_name = serializers.CharField(max_length=100)
    director = serializers.CharField(max_length=100)
    themes = serializers.CharField(max_length=255)
    year = serializers.IntegerField()
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        if hasattr(obj, 'file'):
            return 'movie'
        else:
            return 'serie'