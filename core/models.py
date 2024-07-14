from django.db import models
from uuid import uuid4

class Media(models.Model):
    uuid = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    machine_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=150)
    length = models.IntegerField()
    plot = models.TextField()
    themes = models.CharField(max_length=255)
    year = models.IntegerField()
    imdb_url = models.URLField()

    class Meta:
        abstract = True

class Movie(Media):
    file = models.FileField(upload_to="movies")

    def __str__(self):
        return self.name

class Serie(Media):
    
    def __str__(self):
        return self.name

class Season(models.Model):
    number = models.IntegerField()
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, related_name="seasons")

    def __str__(self):
        return f"{self.serie.name}.S{self.number}"

def episode_file_path(instance, filename):
    return f"series/{instance.season.serie.name}/{instance.season.number}"

class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=150)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name="episodes")
    file = models.FileField(upload_to=episode_file_path)

    def __str__(self):
        return f"{self.season.serie.name}.S{self.season.number}.E{self.number}"
