from django.shortcuts import render
from rest_framework import generics 
from .models import Serie, Movie
from .serializers import MovieSerializer, SerieSerializer
from rest_framework.decorators import api_view
from django.db.models import Q

class MovieDetails(generics.RetrieveAPIView):
    lookup_field = 'machine_name'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SerieDetails(generics.RetrieveAPIView):
    lookup_field = 'uuid'
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class SearchMovies(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        all_records = super().get_queryset()
        query = self.request.GET.get('query')
        results = Movie.objects.none()
        if query:
            results = all_records.filter(Q(name__icontains=query)|Q(machine_name__icontains=query))
        return results 