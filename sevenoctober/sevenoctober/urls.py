"""
URL configuration for sevenoctober project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from theives.views import hello, html, congratulation, print_of_theives
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('helloworld',hello, name='theives.helloworld'),
    # path('celebrate', html , name='celebrate'),
    # path("cong/<user>", congratulation,name="congrate.user"),
    # path('total/<int:num>', print_of_theives, name='print_of_theives')
    ###
    path('theives/', include('theives.urls' )),
    path('tracks/', include('tracks.urls')),
    path('students/', include('students.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
