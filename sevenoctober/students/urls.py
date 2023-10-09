from django.urls import path, include
from students.views import  index
urlpatterns = [

    path('', index, name='students.index'),


]