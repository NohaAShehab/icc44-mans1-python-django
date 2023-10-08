from django.urls import path, include
from tracks.views import  index
urlpatterns = [

   path('',index, name='tracks.index' )

]