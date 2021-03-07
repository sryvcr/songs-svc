import graphene
from songs_svc.songs_app.schemas.songs import Query as QuerySchema, CreateSong


class Query(QuerySchema, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    insert_song = CreateSong.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
