import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from songs_svc.songs_app.models.band import Band as BandModel


class Band(DjangoObjectType):
    class Meta:
        model = BandModel
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'similar_bands': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    all_bands = DjangoFilterConnectionField(Band)
    band = relay.Node.Field(Band)


class CreateBand(relay.ClientIDMutation):
    class Input:
        name = graphene.String(required=True)
        similar_bands = graphene.String()

    band = graphene.Field(Band)

    @classmethod
    def mutate_and_get_payload(cls, root,
                               info, name,
                               similar_bands, client_mutation_id=None):
        new_band = BandModel(name=name, similar_bands=similar_bands)
        new_band.save()
        return CreateBand(band=new_band)
