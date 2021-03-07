"""
execute: 
    src/manage.py shell < src/songs_svc/scripts/upload_data_to_db.py
"""

from django.db import transaction
from songs_svc.utils.get_root_project import get_project_root


@transaction.atomic()
def upload_data(csv_path):
    import csv
    from songs_svc.songs_app.models.songs import Song

    with open(csv_path, 'r') as fp:
        reader = csv.reader(fp)
        next(reader, None)
        count = 0
        for row in reader:
            _, created = Song.objects.get_or_create(
                datetime = row[0],
                external_id = row[1],
                name = row[2],
                album = row[3],
                band = row[4],
                artist = row[5],
                length = row[6],
                genre = row[7],
                subgenre = row[8],
                similar_bands = row[9],
                tags = row[10],
                instruments = row[11],
            )
            count += 1
        print(f'{count} records uploaded to db')

root_project_path = get_project_root()
csv_path = f'{root_project_path}/docs/db/songs_initial_data.csv'
try:
    print('ready to upload data to db')
    upload_data(csv_path)
    print('data uploaded :)')
except Exception as e:
    print('error:', e)
