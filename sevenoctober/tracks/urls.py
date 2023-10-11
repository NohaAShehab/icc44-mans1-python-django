from django.urls import path, include
from tracks.views import  index, create, createViaForm
urlpatterns = [

   path('',index, name='tracks.index' ),
   path('create',create, name='tracks.create' ),
   path('forms/create', createViaForm, name= 'tracks.createform')

]