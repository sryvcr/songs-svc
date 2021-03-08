import uuid
from django.db import models


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    datetime = models.CharField(max_length=30)
    external_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    band = models.ForeignKey('songs_app.Band', related_name='song', on_delete=models.PROTECT)
    artist = models.CharField(max_length=200)
    length = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100, blank=True)
    tags = models.TextField(blank=True)
    instruments = models.TextField(blank=True)
