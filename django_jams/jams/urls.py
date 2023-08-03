from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('artists/', views.ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', views.ArtistRetrieveUpdateDeleteView.as_view(), name='artist-retrieve-update-delete'),

    path('songs/', views.SongListCreateView.as_view(), name='song-list-create'),
    path('songs/<int:pk>/', views.SongRetrieveUpdateDeleteView.as_view(), name='song-retrieve-update-delete'),

    path('genres/', views.GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDeleteView.as_view(), name='genre-retrieve-update-delete'),    
    
    path('albums/', views.AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<int:pk>/', views.AlbumRetrieveUpdateDeleteView.as_view(), name='album-retrieve-update-delete'),

    path('artists-songs/', views.Artists_SongsListCreateView.as_view(), name='artist-songs-list-create'),
    path('artists-songs/<int:pk>/', views.Artists_SongsListCreateView.as_view(), name='artist-songs-retrieve-update-delete'),

    path('artists-albums/', views.Artists_AlbumListCreateView.as_view(), name='artists-albums-list-create'),
    path('artists-albums/<int:pk>/', views.Artists_AlbumRetrieveUpdateDeleteView.as_view(), name='artists-albums-retrieve-update-delete'),

    path('song-artists/', views.Song_ArtistListCreateView.as_view(), name='song-artists-list-create'),
    path('song-artists/<int:pk>/', views.Song_ArtistRetrieveUpdateDeleteView.as_view(), name='song-artists-retrieve-update-delete'),
    
    path('album-songs/', views.Album_SongListCreateView.as_view(), name='album-songs-list-create'),
    path('album-songs/<int:pk>/', views.Album_SongRetrieveUpdateDeleteView.as_view(), name='album-songs-retrieve-update-delete'),
    
    path('user-playlists/', views.User_PlaylistListCreateView.as_view(), name='user-playlists-list-create'),
    path('user-playlists/<int:pk>/', views.User_PlaylistRetrieveUpdateDeleteView.as_view(), name='user-playlists-retrieve-update-delete'),
    
    path('user-playlist-songs/', views.User_Playlist_SongListCreateView.as_view(), name='user-playlist-songs-list-create'),
    path('user-playlist-songs/<int:pk>/', views.User_Playlist_SongRetrieveUpdateDeleteView.as_view(), name='user-playlist-songs-retrieve-update-delete'),
    
    path('plays/', views.PlayListCreateView.as_view(), name='play-list-create'),
    path('plays/<int:pk>/', views.PlayRetrieveUpdateDeleteView.as_view(), name='play-retrieve-update-delete'),


    path('all/', views.AllData.as_view(), name='all')
]

