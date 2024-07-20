from django.urls import path 
from . import views

app_name = 'core'

urlpatterns = [
    path('latest/', views.Latest.as_view(), name="latest_10"),
    path('details/movie/<str:machine_name>/', views.MovieDetails.as_view(), name="movie_details"),
    path('details/serie/<str:machine_name>/', views.SerieDetails.as_view(), name="serie_details"),
    path('search/', views.Search.as_view(), name="search"),
    path('download/movie/<str:machine_name>/', views.DownloadMovie.as_view(), name="download_movie"),
    path('download/serie/<str:machine_name>/', views.DownloadSerie.as_view(), name="download_serie"),
]
