from dataclasses import fields
from rest_framework import serializers
from .models import Artiste, Song, Lyric

class ArtisteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artiste
        fields = ['first_name', 'last_name', 'age']

class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'date_released', 'likes', 'artiste_id']

class LyricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content', 'song_id']