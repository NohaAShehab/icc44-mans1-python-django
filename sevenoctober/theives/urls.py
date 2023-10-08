

from django.urls import path
from theives.views import hello, html, congratulation, print_of_theives
urlpatterns = [

    path('helloworld',hello, name='theives.helloworld'),
    path('celebrate', html , name='celebrate'),
    path("cong/<user>", congratulation,name="congrate.user"),
    path('total/<int:num>', print_of_theives, name='print_of_theives'),

]
