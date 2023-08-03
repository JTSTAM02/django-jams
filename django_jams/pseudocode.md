# Django-Jams

## MoSCoW
    -Must-Haves:
        * DB Diagram
        * CRUD Operations on multiple models
        * Routes to display JSON data
        * Data stored in PostgreSQL database
        * Build API and Routes
        * Use GET, POST, UPDATE, DELETE for routes

    - Should-Haves:
        * Allow user to add a song
        * Different routes for different parameters

    - Could-Haves:
        * Custom field to keep track of plays of song

    - Won't Haves:
        * Hook up to React Frontend



## Questions
    -

## Solutions


## CRUD Functionality (Routes and API)
    - Create:
        * 

    - Read
        * 

    - Update
        * 

    -Delete
        * 


## Models
    - class Artist(models.Model):
        name = models.CharField(max_length=100)

    - class User(models.Model):
        email = models.EmailField(max_length=200)
        username = models.CharField(max_length=100)

    - class Genre(models.Model):
        name = models.CharField(max_length=50)

    - class Song(models.Model):
        name = models.CharField(max_length=200)
        artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    - class Song_Genre(models.Model):
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    - class Artists_Songs(models.Model):
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    - class Artists_Album(models.Model):
        artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
        album = models.ForeignKey(Album, on_delete=models.CASCADE)

    -class Album(models.Model):
         name = models.CharField(max_length=200)

    -class Song_Artist(models.Model):
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    -class Album_Song(models.Model):
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        album = models.ForeignKey(Album, on_delete=models.CASCADE)
        order = models.IntegerField()

    -class User_Playlist(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.ForeignKey(Song, on_delete=models.CASCADE)

    -class User_Playlist_Song(models.Model):
        user_playlist = models.ForeignKey(User_Playlist, on_delete=models.CASCADE)
        song = models.ForeignKey(Song, on_delete=models.CASCADE)

    - class Play(models.Model):
        song = models.ForeignKey(Song, on_delete=models.CASCADE)
        playlist = models.ForeignKey(User_Playlist_Song, on_delete=models.CASCADE)
        played = models.DateTimeField()
        

## Views


## Serializers
    - class ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artist
            fields = '__all__'

    - class UserSerailizer(serializers.ModelSerializer):
        class Meta:
            model= User
            fields = '__all__'

    - class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields= "__all__"

    - class SongSerializer(serializers.ModelSerializer):
        class Meta:
            model = Song
            fields = '__all__'

    - class AlbumSerializer(serializers.ModelSerializer)
        class Meta:
            model = Album
            fields = '__all_

    - class Song_GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Song_Genre
            fields = '__all_'

    - class Artists_SongSerializer(serializers.ModelSerializer):
        class Meta:
            model = Artists_Songs
            fields = '__all__'

    - class Artists_AlbumSerializer(serializers.ModelSerializer):
        class Meta:
            model =
            fields = 

    - class Artists_SongSerializer(serializers.ModelSerializer):
        class Meta:
            model =
            fields = 

    - class Artists_SongSerializer(serializers.ModelSerializer):
        class Meta:
            model =
            fields = 

    - class Artists_SongSerializer(serializers.ModelSerializer):
        class Meta:
            model =
            fields = 


## EndPoints (URL's and Routes)



## Database Schema/Table Relationships