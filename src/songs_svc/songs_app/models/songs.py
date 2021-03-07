from django.db import models
import uuid


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    datetime = models.CharField(max_length=30)
    external_id = models.IntegerField()
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    band = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    length = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    subgenre = models.CharField(max_length=100)
    similar_bands = models.TextField()
    tags = models.TextField()
    instruments = models.TextField()

    def __str__(self):
        return self.name
