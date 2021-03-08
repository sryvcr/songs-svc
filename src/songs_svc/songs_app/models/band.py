import uuid
from django.db import models


class Band(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    similar_bands = models.TextField(blank=True)
