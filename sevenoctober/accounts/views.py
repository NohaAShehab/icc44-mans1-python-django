from django.shortcuts import render, redirect, reverse

from django.views.generic.edit import CreateView
from django.contrib.auth.models import  User
from accounts.forms import  CustomizedUserCreationForm
from django.urls import reverse_lazy
# Create your views here.



def profile(request):
    return  redirect('/posts/')



# class

class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/registeration.html'
    form_class = CustomizedUserCreationForm
    # login_url = reverse('login')
    success_url = reverse_lazy("login")