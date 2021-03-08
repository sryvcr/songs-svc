from django.test import TestCase
from django.db.models import Max
from songs_svc.songs_app.models.song import Song
from songs_svc.songs_app.models.band import Band
from songs_svc.schema import schema

class TestSongs(TestCase):

    def setUp(self):
        band1 = Band(
            name='test111',
            similar_bands='test111111'
        )
        band1.save()
        song1 = Song(
            datetime='04/08/20 11:50PM',
            external_id=1,
            name='test1',
            album='test11',
            band=band1,
            artist='test',
            length='02:22',
            genre='test1111',
            subgenre='test11111',
            tags='test',
            instruments='test',
        )
        song1.save()

    def test_get_song_filters(self):
        query = """
            query {
                allSongs(
                    name_Icontains: "test1",
                    album_Icontains: "test11",
                    band_Name_Icontains: "test111",
                    genre_Icontains: "test1111", 
                    subgenre_Icontains: "test11111",
                    band_SimilarBands_Icontains: "test111111"
                ) {
                    edges {
                        node {
                            name,
                            album,
                            length,
                            genre,
                            subgenre,
                            tags,
                            instruments,
                            band {
                                name,
                                similarBands
                            }
                        }
                    }
                }
            }
        """
        expected = {
            "allSongs": {
                "edges": [
                    {
                        "node": {
                            "name": "test1",
                            "album": "test11",
                            "length": "02:22",
                            "genre": "test1111",
                            "subgenre": "test11111",
                            "tags": "test",
                            "instruments": "test",
                            "band": {
                                "name": "test111",
                                "similarBands": "test111111"
                            }
                        }
                    }
                ]
            }
        }
        result = schema.execute(query)
        assert not result.errors
        assert result.data == expected

    def test_mutation_song(self):
        external_id_max = Song.objects.aggregate(Max('external_id'))['external_id__max']
        external_id = 1 if external_id_max == None else int(external_id_max) + 1
        mutation = """
            mutation MyMutation {
                insertSong(input: {
                    clientMutationId: "1",
                    datetime: "07/03/21 06:31PM",
                    externalId: %s,
                    name: "prueba",
                    album: "prueba",
                    band: "test111",
                    artist: "prueba",
                    length: "02:55",
                    genre: "prueba",
                    subgenre: "prueba",
                    tags: "prueba",
                    instruments: "prueba",
                }) {
                        song {
                            datetime
                            externalId
                            name
                            album
                            artist
                            length
                            genre
                            subgenre
                            tags
                            instruments,
                            band {
                                name
                            }
                        }
                    }
            }
        """ % external_id
        expected = {
            "insertSong": {
                "song": {
                    "datetime": "07/03/21 06:31PM",
                    "externalId": external_id,
                    "name": "prueba",
                    "album": "prueba",
                    "artist": "prueba",
                    "length": "02:55",
                    "genre": "prueba",
                    "subgenre": "prueba",
                    "tags": "prueba",
                    "instruments": "prueba",
                    "band": {
                        "name": "test111"
                    }
                }
            }
        }
        result = schema.execute(mutation)
        assert not result.errors
        assert dict(result.data) == expected
