import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from songs_svc.songs_app.models.songs import Song as SongModel


class Song(DjangoObjectType):
    class Meta:
        model = SongModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'album': ['exact', 'icontains', 'istartswith'],
            'band': ['exact', 'icontains', 'istartswith'],
            'genre': ['exact', 'icontains', 'istartswith'],
            'subgenre': ['exact', 'icontains', 'istartswith'],
            'similar_bands': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    all_songs = DjangoFilterConnectionField(Song)
    song = relay.Node.Field(Song)


class CreateSong(relay.ClientIDMutation):
    class Input:
        datetime = graphene.String(required=True)
        external_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        album = graphene.String(required=True)
        band = graphene.String(required=True)
        artist = graphene.String(required=True)
        length = graphene.String(required=True)
        genre = graphene.String(required=True)
        subgenre = graphene.String()
        similar_bands = graphene.String()
        tags = graphene.String()
        instruments = graphene.String()

    song = graphene.Field(Song)

    @classmethod
    def mutate_and_get_payload(cls, root,
                               info, datetime,
                               external_id, name,
                               album, band,
                               artist, length,
                               genre, subgenre,
                               similar_bands, tags,
                               instruments, client_mutation_id=None):
        new_song = SongModel(datetime=datetime, external_id=external_id,
                        name=name, album=album,
                        band=band, artist=artist,
                        length=length, genre=genre,
                        subgenre=subgenre, similar_bands=similar_bands,
                        tags=tags, instruments=instruments)
        new_song.save()
        return CreateSong(song=new_song)
