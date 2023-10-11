from django.urls import path, include
from tracks.views import  index, create
urlpatterns = [

   path('',index, name='tracks.index' ),
   path('create',create, name='tracks.create' )

]