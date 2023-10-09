from django.db import models

# Create your models here.


class Student(models.Model):
    # define properties of student model object
    "name, age, email, image, created , updated at"
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=10, null=True)
    email = models.EmailField(null=True, unique=True)
    image = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
