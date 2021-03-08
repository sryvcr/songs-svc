from django.test import TestCase
from songs_svc.songs_app.models.band import Band
from songs_svc.schema import schema

class TestBands(TestCase):

    def setUp(self):
        band1 = Band(
            name='prueba',
            similar_bands='prueba similar'
        )
        band1.save()

    def test_get_band_filters(self):
        query = """
            query {
                allBands(
                    name_Icontains: "prueba",
                    similarBands_Icontains: "prueba similar"
                ) {
                    edges {
                        node {
                            name,
                            similarBands,
                        }
                    }
                }
            }
        """
        expected = {
            "allBands": {
                "edges": [
                    {
                        "node": {
                            "name": "prueba",
                            "similarBands": "prueba similar"
                        }
                    }
                ]
            }
        }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected


    def test_mutation_band(self):
        mutation = """
            mutation MyMutation {
                insertBand(input: {
                    clientMutationId: "1"
                    name: "prueba",
                    similarBands: "prueba",
                }) {
                        band {
                            name
                            similarBands
                        }
                    }
            }
        """
        expected = {
            "insertBand": {
                "band": {
                    "name": "prueba",
                    "similarBands": "prueba"
                }
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert result.data == expected