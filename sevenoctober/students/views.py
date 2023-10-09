from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.http import HttpResponse

from students.models import Student
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