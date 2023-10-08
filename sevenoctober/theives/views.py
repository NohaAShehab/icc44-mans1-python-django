from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# functional views


def hello(request):
    return HttpResponse("Hello world !!! ")

def html(request):
    return HttpResponse("<h1 style='color:green'> Haya Allah Al-Moqwama </h1>")



def index(request):
    return render(request, 'theives/index.html', context={"theives":theives})

def congratulation(request,user ):
    return  HttpResponse(f"<h1> Congratulations  {user} </h1>")


def print_of_theives(request, num):
    print(type(num))
    num = int(num) *10
    return HttpResponse(f"<h2>total number = {num} </h2>")




theives = [
    {"id":1, "name":"test", "image":"pic1.png"},
    {"id":2, "name":"abc", "image":"pic2.png"},
    {"id":3, "name":"jj", "image":"pic3.png"},
    {"id":4, "name":"mmm", "image":"pic4.png"}
]



def listt(request):
    return HttpResponse(theives)


def profile(request, id):
    theif = filter(lambda th:th['id']==id , theives)  #
    # print(theif)
    theif = list(theif)
    if theif:
        print(theif[0])
        return HttpResponse(theif[0])

    return HttpResponse("Sorry target theif profile not found ")




