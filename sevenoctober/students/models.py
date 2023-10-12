from django.db import models
from django.shortcuts import reverse
# Create your models here.
from tracks.models import Track

class Student(models.Model):
    # define properties of student model object
    "name, age, email, image, created , updated at"
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=10, null=True)
    email = models.EmailField(null=True, unique=True)
    image = models.ImageField(upload_to='students/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ######## backword relation
    track = models.ForeignKey(Track, null=True, blank=True,
                              on_delete=models.CASCADE, related_name='students')
    ## student.track ===> Track object


    def __str__(self):
        return f"{self.name}"


    def get_show_url(self):
        return  reverse('students.show', args=[self.id])


    def get_delete_url(self):
        return  reverse('students.delete', args=[self.id])


    def get_image_url(self):
        return f"/media/{self.image}"


    def get_edit_url(self):
        return  reverse('students.edit', args=[self.id])


    @classmethod
    def get_sepcific_object(cls, id):
        return  cls.objects.get(id=id)



