from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import time
import random
from datetime import timedelta, date, datetime
from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse ## NEW

# Create your views here.
def home_page_view(request):
  return HttpResponse("Homepage")

class ShowAllProfilesView(ListView):
  '''A view to show all ARticles.'''

  model = Profile
  template_name = 'mini_fb/show_all_profiles.html'
  context_object_name = 'profiles'

def info_page(request):

  template_name = "mini_fb/info.html"

  context = {
    'current_time': time.ctime(),
  }

  return render(request,template_name,context)

class ShowProfilePageView(DetailView):
  model = Profile 
  template_name = 'mini_fb/show_profile.html'
  context_object_name = 'profile'


class CreateProfileView(CreateView):
  form_class = CreateProfileForm

  template_name = 'mini_fb/create_profile_form.html'

  def get_absolute_url(self) -> str:
    '''Return the URL to redirect to after successfully submitting form.'''
    return reverse('profile',kwargs={'pk': self.kwargs['pk']})




