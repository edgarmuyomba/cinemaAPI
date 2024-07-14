from django.shortcuts import render
from rest_framework import generics 
from .models import Serie, Movie
from .serializers import MovieSerializer, SerieSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
class MovieDetails(generics.RetrieveAPIView):
    lookup_field = 'machine_name'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET'])
class SerieDetails(generics.RetrieveAPIView):
    lookup_field = 'uuid'
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

@api_view(['GET'])
class Search(generics.ListAPIView):
    pass