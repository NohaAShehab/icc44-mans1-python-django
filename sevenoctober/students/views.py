from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponse

from students.models import Student
from tracks.models import Track
from students.forms import StudentForm
# Create your views here.


def index(request):

    students = Student.objects.all()

    return  render(request, 'students/index.html', context={"students":students})


def show(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/show.html', context={"student":student})


def delete(request, id ):
    student = Student.objects.get(id=id)
    student.delete()
    # return HttpResponse("deleted")
    url = reverse('students.index')
    return redirect(url)


def create(request):
    # print(request)
    if request.method == 'POST':
        # get data from the request body
        print(request.POST)
        name = request.POST['name']
        age = request.POST['age']
        email= request.POST['email']
        image = request.POST['image']
        # then add it to the database
        student = Student()
        student.name= name
        student.age= age
        student.email= email
        student.image= image
        student.save()
        # return HttpResponse("Student added successfully")
        # url = reverse('students.index')
        # return redirect(url)
        print(student.get_show_url())
        # url = reverse('students.show' , args=[student.id])
        # return redirect(url)
        return redirect(student.get_show_url())


    return  render(request, 'students/create.html')


def createViaForm(request):
    form = StudentForm()
    if request.method == 'POST':
        print(request.POST)
        form  = StudentForm(request.POST)
        track = None
        if request.POST['track']:
            track = Track.objects.get(id=request.POST['track'])
        if form.is_valid():
            student = Student.objects.create(name=request.POST['name'], age=request.POST['age'],
                                             image=request.POST['image'], email=request.POST['email'],
                                             track = track)
            return redirect(student.get_show_url())

        # return HttpResponse("data received")

    return  render(request, 'students/forms/create.html',
                   context={"form":form})
