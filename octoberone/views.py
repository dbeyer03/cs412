from django.shortcuts import render

# Create your views here.
from . models import *
from django.views.generic import ListView

class ShowAllView(ListView):
  '''A view to show all ARticles.'''

  model = Article 
  template_name = 'octoberone/show_all.html'
  context_object_name = 'articles'