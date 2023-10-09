from django.contrib import admin

# Register your models here.
from students.models import Student

admin.site.register(Student)