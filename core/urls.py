from django.urls import path 
from . import views

app_name = 'core'

urlpatterns = [
    path('details/movie/<str:machine_name>/', views.MovieDetails.as_view(), name="movie_details"),
    path('details/serie/<str:machine_name>/', views.SerieDetails.as_view(), name="serie_details"),
    path('search/movie/', views.SearchMovies.as_view(), name="search_movies"),
    path('search/serie/', views.SearchSeries.as_view(), name="search_series"),
]
