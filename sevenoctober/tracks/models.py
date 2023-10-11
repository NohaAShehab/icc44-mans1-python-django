from django.db import models
from django.shortcuts import  reverse
# Create your models here.


class Track(models.Model):
    name= models.CharField(max_length=100, unique=True)
    description=  models.CharField(max_length=200,null=True, blank=True)
    # upload file in folder media --> in the project
    image = models.ImageField(upload_to='tracks/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_all_tracks(cls):
        return  cls.objects.all()


    @classmethod
    def get_index_url(cls):
        return reverse('tracks.index')


    def get_image_url(self):
        return f"/media/{self.image}"