from django.db import models
import uuid


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    datetime = models.CharField(max_length=30)
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    band = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    length = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100, blank=True)
    similar_bands = models.TextField(blank=True)
    tags = models.TextField(blank=True)
    instruments = models.TextField(blank=True)

    def __str__(self):
        return self.name
