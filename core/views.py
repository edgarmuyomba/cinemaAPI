from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from .models import Serie, Movie
from .serializers import MovieSerializer, SerieSerializer, MediaSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.response import Response
from itertools import chain
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse

class MovieDetails(generics.RetrieveAPIView):
    lookup_field = 'machine_name'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SerieDetails(generics.RetrieveAPIView):
    lookup_field = 'machine_name'
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

class Search(APIView):
    def get(self, request):
        query = request.GET.get('query')
        if query:
            queryset1 = Movie.objects.filter(Q(name__icontains=query)|Q(machine_name__icontains=query))
            queryset2 = Serie.objects.filter(Q(name__icontains=query)|Q(machine_name__icontains=query))
            results = list(chain(queryset1, queryset2))
        else:
            results = []
        response = MediaSerializer(results, many=True)
        return Response(response.data)
    
class DownloadMovie(APIView):
    def get(self, request, *args, **kwargs):
        machine_name = kwargs['machine_name']
        movie = get_object_or_404(Movie, machine_name=machine_name)
        response = StreamingHttpResponse(open(movie.file.path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{movie.name}.mp4"'
        return response