from django.db import models

class Artist(models.Model):
        name = models.CharField(max_length=100)

class Users(models.Model):
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=100)

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist, through="Artists_Songs")
    genres = models.ManyToManyField(Genre, through="Song_Genre")

class Song_Genre(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Artists_Songs(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Album(models.Model):
    name = models.CharField(max_length=200)

class Artists_Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

class Song_Artist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Album_Song(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    order = models.IntegerField()

class User_Playlist(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.ForeignKey(Song, on_delete=models.CASCADE)

class User_Playlist_Song(models.Model):
    user_playlist = models.ForeignKey(User_Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class Play(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(User_Playlist_Song, on_delete=models.CASCADE)
    played = models.DateTimeField()