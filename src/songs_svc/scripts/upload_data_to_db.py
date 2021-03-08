"""
execute: 
    src/manage.py shell < src/songs_svc/scripts/upload_data_to_db.py
"""

from django.db import transaction
from songs_svc.utils.get_root_project import get_project_root


@transaction.atomic()
def upload_data(csv_path):
    import csv
    from songs_svc.songs_app.models.song import Song
    from songs_svc.songs_app.models.band import Band

    with open(csv_path, 'r') as fp:
        reader = csv.reader(fp)
        next(reader, None)
        bands_uploaded = 0
        songs_uploaded = 0
        for row in reader:
            band, band_created = Band.objects.get_or_create(
                name = row[4] if row[4] != "" else [5],
            )
            band.similar_bands = row[9] if  band.similar_bands == "" else f'{band.similar_bands}; {row[9]},'
            band.save()
            if band_created:
                bands_uploaded += 1
            song, song_created = Song.objects.get_or_create(
                datetime = row[0],
                external_id = row[1],
                name = row[2],
                album = row[3],
                band = band,
                artist = row[5],
                length = row[6],
                genre = row[7],
                subgenre = row[8],
                tags = row[10],
                instruments = row[11],
            )
            songs_uploaded += 1
        print(f'{bands_uploaded} bands uploaded to db')
        print(f'{songs_uploaded} songs uploaded to db')

root_project_path = get_project_root()
csv_path = f'{root_project_path}/docs/db/songs_initial_data.csv'
try:
    print('ready to upload data to db')
    upload_data(csv_path)
    print('data uploaded :)')
except Exception as e:
    print('error:', e)
