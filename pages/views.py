from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,TemplateView


class homepageview(ListView): # it returns a thing called object_list , it is a list 
    model = Post
    context_object_name = 'list' # we can use the alternate of object_list and can store context_object_name in any name 
    template_name = 'pages/index.html'


class About(TemplateView):
    template_name = 'pages/about.html'
