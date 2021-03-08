import graphene
from songs_svc.songs_app.schemas.songs import Query as QuerySongs, CreateSong
from songs_svc.songs_app.schemas.bands import Query as QueryBands, CreateBand


class Query(QuerySongs, QueryBands, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    insert_song = CreateSong.Field()
    insert_band = CreateBand.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
