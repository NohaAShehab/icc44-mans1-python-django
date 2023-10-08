

from django.urls import path
from theives.views import (hello, html, congratulation, print_of_theives,
                           listt, profile, index)
urlpatterns = [

    path('helloworld',hello, name='theives.helloworld'),
    path('celebrate', html , name='celebrate'),
    path("cong/<user>", congratulation,name="congrate.user"),
    path('total/<int:num>', print_of_theives, name='print_of_theives'),
    path('list',listt, name='theives.list' ),
    path('profile/<int:id>', profile, name='theif.profile'),
    path('index', index, name='theives.index')

]
