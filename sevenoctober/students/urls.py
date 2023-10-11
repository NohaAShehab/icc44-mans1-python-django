from django.urls import path, include
from students.views import  index, show, delete, create,createViaForm
urlpatterns = [

    path('', index, name='students.index'),
    path('<int:id>', show, name='students.show'),
    path('<int:id>/delete', delete, name='students.delete'),
    path('create', create, name='students.create'),
    path('forms/create', createViaForm, name='students.forms.create')


]