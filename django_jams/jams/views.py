from rest_framework import generics
from .models import Artist, Album, Genre, Song, Song_Genre, Artists_Songs, Artists_Album, Album_Song, Song_Artist, Play, User_Playlist, User_Playlist_Song
from .serializers import ArtistSerializer, AlbumSerializer, GenreSerializer, SongSerializer, Song_GenreSerializer, Artists_SongSerializer, Artists_AlbumSerializer, Song_ArtistSerializer, Album_SongSerializer, PlaySerializer, User_Playlist_SongSerializer, User_PlaylistSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class Song_GenreListCreateView(generics.ListCreateAPIView):
    queryset = Song_Genre.objects.all()
    serializer_class = Song_GenreSerializer

class Song_GenreRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song_Genre.objects.all()
    serializer_class = Song_GenreSerializer

class Artists_SongsListCreateView(generics.ListCreateAPIView):
    queryset = Artists_Songs.objects.all()
    serializer_class = Artists_SongSerializer

class Artists_SongsRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artists_Songs.objects.all()
    serializer_class = Artists_SongSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class Artists_AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Artists_Album.objects.all()
    serializer_class = Artists_AlbumSerializer

class Artists_AlbumRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artists_Album.objects.all()
    serializer_class = Artists_AlbumSerializer

class Song_ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Song_Artist.objects.all()
    serializer_class = Song_ArtistSerializer

class Song_ArtistRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song_Artist.objects.all()
    serializer_class = Song_ArtistSerializer

class Album_SongListCreateView(generics.ListCreateAPIView):
    queryset = Album_Song.objects.all()
    serializer_class = Album_SongSerializer

class Album_SongRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album_Song.objects.all()
    serializer_class = Album_SongSerializer

class User_PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = User_Playlist.objects.all()
    serializer_class = User_PlaylistSerializer

class User_PlaylistRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Playlist.objects.all()
    serializer_class = User_PlaylistSerializer

class User_Playlist_SongListCreateView(generics.ListCreateAPIView):
    queryset = User_Playlist_Song.objects.all()
    serializer_class = User_Playlist_SongSerializer

class User_Playlist_SongRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_Playlist_Song.objects.all()
    serializer_class = User_Playlist_SongSerializer

class PlayListCreateView(generics.ListCreateAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

class PlayRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

class AllData(APIView):
    def get(self):
        artists = Artist.objects.all()
        albums = Album.objects.all()
        genres = Genre.objects.all()
        songs = Song.objects.all()

        artist_serializer = ArtistSerializer(artists, many=True)
        album_serializer = AlbumSerializer(albums, many=True)
        genre_serializer = GenreSerializer(genres, many=True)
        song_serializer = SongSerializer(songs, many=True)

        data = {
            'artists': artist_serializer.data,
            'albums': album_serializer.data,
            'genres': genre_serializer.data,
            'songs': song_serializer.data,
        }

        return Response(data)