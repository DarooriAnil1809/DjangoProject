from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician

# Create your views here.
def MusicIndex(request):
    #hello world example
    #return HttpResponse("HELLO MUSIC WORLD")
    music_list = Musician.objects.all()
    context = {
        'music_list':music_list,
    }
    return render(request, 'MusicApp/music.html', context)


