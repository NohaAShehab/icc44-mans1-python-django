from django.shortcuts import render, redirect, reverse
from tracks.models import Track
from django.http import HttpResponse
from  tracks.forms import  TrackForm
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
        url = reverse('tracks.index') # /tracks/
        return redirect(url)
        # return redirect('/tracks/')

        # return HttpResponse("data received")
    return  render(request, 'tracks/create.html')




def createViaForm(request):
    # django --> create html for
    form = TrackForm()

    if request.POST:
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST['name']
            description = request.POST['description']
            image = request.FILES['image']
            track = Track.objects.create(name=name, image=image, description=description)
            url = reverse('tracks.index')  # /tracks/
            return redirect(url)

    return  render( request, 'tracks/forms/create.html',
                    context={"form": form})
