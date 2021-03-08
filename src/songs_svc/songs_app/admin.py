from django.contrib import admin
from .models.song import Song
from .models.band import Band


admin.site.register(Song)
admin.site.register(Band)
