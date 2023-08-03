from rest_framework import serializers
from .models import *

class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = '__all__'

class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields= "__all__"

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all_'

class Song_GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song_Genre
        fields = '__all_'

class Artists_SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists_Songs
        fields = '__all__'

class Artists_AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists_Album
        fields = '__all_'

class Song_ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song_Artist
        fields = '__all__'

class Album_SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album_Song
        fields = '__all__'

class User_PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Playlist
        fields = '__all__'

class User_Playlist_SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Playlist_Song
        fields = '__all__'

class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'