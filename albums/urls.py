from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('album/new/', views.album_new, name='album_new'),
    path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
    path('album/<int:pk>/delete/', views.album_delete, name = 'album_delete'),
    path('artist/<int:artist_pk>/', views.albums_by_artist, name = 'albums_by_artist'),
    path('allartists/', views.artist_list, name = 'artist_list'),
    path('allartists/<int:pk>/', views.artist_detail, name = 'artist_detail'),

]