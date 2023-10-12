from django.shortcuts import  reverse
from django.db import models
from students.models import Student

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    image= models.ImageField(upload_to='posts/images/', null=True , blank=True)
    author = models.ForeignKey(Student, null=True, blank=True, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'


    def get_image_url(self):
        return f'/media/{self.image}'



    def get_show_url(self):
        return  reverse('posts.details', args=[self.id])

    def get_edit_url(self):
        return  reverse('posts.edit', args=[self.id])

    def get_delete_url(self):
        return  reverse('posts.delete', args=[self.id])