from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Album, Musician
from .forms import AlbumForm
# from django.shortcuts import redirect

# Create your views here.
def album_list(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_list.html', {'albums': albums})

def artist_list(request):
    albums = Album.objects.all()
    musicians = Musician.objects.all()
    return render(request, 'albums/artist_list.html', {'musicians': musicians, 'albums': albums })

def album_detail(request,pk):
    album= get_object_or_404(Album, pk=pk)
    musicians = Musician.objects.all()
    return render(request, 'albums/album_detail.html', {'album': album, 'musicians': musicians })

def artist_detail(request,pk):
    musician = get_object_or_404(Musician, pk=pk)
    albums = Album.objects.filter(artist_id=pk)
    context = {
        'musician': musician,
        'albums': albums
    }
    return render(request, 'albums/artist_detail.html', context)

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            # album.artist = request.Musician
            album.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'albums/album_edit.html', {'form': form})

def album_edit(request,pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save(commit=False)
            # album.artist = request.Musician
            album.save()
            return redirect('album_detail', pk=pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html',{'form': form})

def album_delete(request,pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return redirect('album_list')

def albums_by_artist(request, artist_pk):
    albums = Album.objects.filter(artist_id = artist_pk)
    musician = get_object_or_404(Musician, pk = artist_pk)
    context = {
        'albums': albums,
        'musician': musician
    }
    return render(request, 'albums/albums_by_artist.html', context)


    

