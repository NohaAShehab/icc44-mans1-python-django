from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# functional views


def hello(request):
    return HttpResponse("Hello world !!! ")

def html(request):
    return HttpResponse("<h1 style='color:green'> Haya Allah Al-Moqwama </h1>")


def congratulation(request,user ):
    return  HttpResponse(f"<h1> Congratulations  {user} </h1>")


def print_of_theives(request, num):
    print(type(num))
    num = int(num) *10
    return HttpResponse(f"<h2>total number = {num} </h2>")