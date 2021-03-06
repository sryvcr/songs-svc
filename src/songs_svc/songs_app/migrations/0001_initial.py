# Generated by Django 3.0.8 on 2021-03-08 00:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('similar_bands', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('datetime', models.CharField(max_length=30)),
                ('external_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('length', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=100)),
                ('subgenre', models.CharField(blank=True, max_length=100)),
                ('tags', models.TextField(blank=True)),
                ('instruments', models.TextField(blank=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='song', to='songs_app.Band')),
            ],
        ),
    ]
