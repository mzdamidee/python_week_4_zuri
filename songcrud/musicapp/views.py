from .models import Artiste, Song, Lyric
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer


# Create your views here.

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all().order_by('first_name')
    serializer_class = ArtisteSerializer
    permission_classes = [permissions.IsAuthenticated]

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

class LyricViewSet(viewsets.ModelViewSet):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    permission_classes = [permissions.IsAuthenticated]