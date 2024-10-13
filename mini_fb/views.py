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

class CreateStatusMessageView(CreateView):
  form_class = CreateStatusMessageForm 
  template_name = 'mini_fb/create_status_form.html'

  def get_context_data(self, **kwargs: any) -> dict[str,any]:

    context = super().get_context_data(**kwargs)

    profile = Profile.objects.get(pk=self.kwargs['pk'])

    context['profile'] = profile 
    return context

  def form_valid(self,form):

    print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
    print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

    # find the Profile indicated by the PK from the url pattern.
    profile = Profile.objects.get(pk=self.kwargs['pk'])

    # Attach Profile to instant of comment to set FK
    form.instance.profile = profile 

    # delegate work to superclass version of method
    return super().form_valid(form)

  def get_success_url(self) -> str: 

    #redirects the URL on success.
    profile = Profile.objects.get(pk=self.kwargs['pk'])
    return reverse('show_profile',kwargs={'pk':profile.pk})
  

  

  




