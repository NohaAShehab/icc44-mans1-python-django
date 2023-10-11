from django.shortcuts import render, redirect
from tracks.models import Track
from django.http import HttpResponse
# Create your views here.


def index(request):
    # tracks = Track.objects.all()
    tracks= Track.get_all_tracks()
    return render(request,
                  'tracks/index.html', {"tracks":tracks})


def create(request):
    if request.POST:
        print(request.POST)
        print(request.FILES)
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']
        track = Track.objects.create(name=name, image=image, description=description)
        return redirect(Track.get_index_url())

        # return HttpResponse("data received")
    return  render(request, 'tracks/create.html')