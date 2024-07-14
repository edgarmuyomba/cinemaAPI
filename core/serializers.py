from rest_framework.serializers import ModelSerializer
from .models import Serie, Movie 

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie 
        fields = "__all__"

class SerieSerializer(ModelSerializer):
    class Meta:
        model = Serie 
        fields = "__all__"