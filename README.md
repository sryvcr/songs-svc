## Songs Service

### How to run app

1. Clone repository
```sh
$ mkdir songs-svc
$ cd songs-svc
$ virtualenv . -p python3
$ git clone https://github.com/sryvcr/starwarsfansite.git
$ source /bin/activate
(songs-svc)$ cd songs-svc
```

2. Apply requirements
```sh
(songs-svc)$ pip install -r requirements.txt
```

3. Run server
```sh
(songs-svc)$ src/manage.py runserver
```

3. Upload initial data to db
```sh
(songs-svc)$ src/manage.py migrate
(songs-svc)$ src/manage.py shell < src/songs_svc/scripts/upload_data_to_db.py
```

### API Requests
Note: in dit src/docs/postman you can find a postman collection file

#### Query songs
```javascript
query {
    allSongs(
        name_Icontains: "test",
        album_Icontains: "test",
        band_Name_Icontains: "test",
        genre_Icontains: "test", 
        subgenre_Icontains: "test",
        band_SimilarBands_Icontains: "test"
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
```

#### Query bands
```javascript
query {
    allBands(
        name_Icontains: "test",
        similarBands_Icontains: "test"
    ) {
        edges {
            node {
                name,
                similarBands,
                song {
                    edges {
                        node {
                            name,
                        }
                    }
                }
            }
        }
    }
}
```

#### Mutation song
```javascript
mutation MyMutation {
    insertSong(input: { 
        clientMutationId: "1",
        datetime: "07/03/21 06:31PM",
        externalId: 1,
        name: "test",
        album: "test",
        band: "test",
        artist: "test",
        length: "02:55",
        genre: "test",
        subgenre: "test",
        tags: "test",
        instruments: "test",
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
```

#### Mutation band
```javascript
mutation MyMutation {
    insertBand(input: { 
        clientMutationId: "1"
        name: "test",
        similarBands: "test",
}) {
        band {
            name
            similarBands
        }
    }
}
```
