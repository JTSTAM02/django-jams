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



## AGILE STORIES
  -As an user I want to be able to see my songs, so that I can click on songs to listen to
  -As an user I want to be able to add new songs, so that I can hear new music
  -As an user I want to be able to see how many times a song has been played, so that I know how often I listen to a song
  -As an user I want to be able to delete songs, so that my library does not become too full

## CRUD
    - Create: 
        * POST- enter new information

    - Read: 
        * GET- display information within given table

    - Update: 
        * PUT- add data to existing tables
    - Delete: 
        * DELETE- remove tables/information
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

    -class AuthorListCreateView(generics.ListCreateAPIView):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

    - class AuthorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

    - class UserListCreateView(generics.ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

    - class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

    - class GenreListCreateView(generics.ListCreateAPIView):
        queryset = Genre.objects.all()
        serializer_class = GenreSerializer

    -class GenreRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Genre.objects.all()
        serializer_class = GenreSerializer

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
            model = Artists_Album
            fields = '__all_'

    - class Song_ArtistSerializer(serializers.ModelSerializer):
        class Meta:
            model = Song_Artist
            fields = '__all__'

    - class Album_SongSerializer(serializers.ModelSerializer):
        class Meta:
            model = Album_Song
            fields = '__all__'

    - class User_PlaylistSerializer(serializers.ModelSerializer):
        class Meta:
            model = User_Playlist
            fields = '__all__'

    - class User_Playlist_SongSerializer(serializers.ModelSerializer):
        class Meta:
            model = User_Playlist_Song
            fields = '__all__'

    -class PlaySerializer(serializers.ModelSerializer):
        class Meta:
            model = Play
            fields = '__all__'


## EndPoints (URL's and Routes)
   ### GET:
    -api/artist/
    -/api/artist/<artist_id>/
    -api/genres
    -api/genres/<genre_id>/


## Database Schema/Table Relationships

see https://dbdiagram.io/d/64c15c9802bd1c4a5ebffe5e 