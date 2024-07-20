from rest_framework import generics 
from rest_framework.views import APIView
from .models import Serie, Movie, Season, Episode
from .serializers import MovieSerializer, SerieSerializer, MediaSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.response import Response
from itertools import chain
from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse, Http404
from rest_framework.permissions import IsAuthenticated

class Latest(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self):
        movies = Movie.objects.all()[:5]
        series = Serie.objects.all()[:5]
        all = list(chain(movies, series))
        response = MediaSerializer(all, many=True)
        return Response(response.data)

class MovieDetails(generics.RetrieveAPIView):
    lookup_field = 'machine_name'
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

class SerieDetails(generics.RetrieveAPIView):
    lookup_field = 'machine_name'
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = [IsAuthenticated]

class Search(APIView):
    
    permission_classes = [IsAuthenticated]

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
    
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        machine_name = kwargs['machine_name']
        movie = get_object_or_404(Movie, machine_name=machine_name)

        filepath = movie.file.path
        response = StreamingHttpResponse(open(filepath, 'rb'))

        with open(filepath, 'rb') as file:
            file_data = file.read()

        response['Content-Length'] = len(file_data)

        response['Content-Disposition'] = f'attachment; filename="{movie.name}.mp4"'
        return response
    
class DownloadSerie(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        machine_name = kwargs['machine_name']
        try:
            season_no, episode_no = int(request.GET['season']), int(request.GET['episode'])
        except:
            raise Http404("Please provide a season and episode specification")
        else:
            serie = get_object_or_404(Serie, machine_name=machine_name)
            try:
                season = serie.seasons.get(number=season_no)
            except Season.DoesNotExist:
                raise Http404(f"{serie.name} Season {season_no} not yet available.")
            else:
                try:
                    episode = season.episodes.get(number=episode_no)
                except Episode.DoesNotExist:
                    raise Http404(f"{serie.name} Season {season_no} Episode {episode_no} not yet available.")
                else:
                    filepath = episode.file.path
                    response = StreamingHttpResponse(open(filepath, 'rb'))
                    response['Content-Disposition'] = f'attachment; name="{serie.name}"; filename="{episode.name}.mp4"; season="{season_no}"'

                    with open(filepath, 'rb') as file:
                        file_data = file.read()
                    
                    response['Content-Length'] = len(file_data)

                    return response