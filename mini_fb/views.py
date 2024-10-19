from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import time
import random
from datetime import timedelta, date, datetime
from . models import *
from . forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse ## NEW
from .forms import UpdateProfileForm

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
  '''A view to show an individual profile page.'''
  model = Profile 
  template_name = 'mini_fb/show_profile.html'
  context_object_name = 'profile'


class CreateProfileView(CreateView):
  '''A view to create a new profile page.'''
  form_class = CreateProfileForm
  template_name = 'mini_fb/create_profile_form.html'

class CreateStatusMessageView(CreateView):
  '''A view to create a status message on a profile page.'''
  form_class = CreateStatusMessageForm 
  template_name = 'mini_fb/create_status_form.html'

  def get_context_data(self, **kwargs: any) -> dict[str,any]:

    # identify profile by its kwargs.
    context = super().get_context_data(**kwargs)
    profile = Profile.objects.get(pk=self.kwargs['pk'])
    # store kwargs info in dictionary.
    context['profile'] = profile 

    return context

  def form_valid(self,form):

    print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
    print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

    # find the Profile indicated by the PK from the url pattern.
    profile = Profile.objects.get(pk=self.kwargs['pk'])

    # Attach Profile to instance of comment to set FK
    form.instance.profile = profile 

    # save the status message to database
    sm = form.save()

    # read the file from the form:
    files = self.request.FILES.getlist('files')

    # for each file in files
    for file in files:
      add_image = Image()
      add_image.image_file = file
      add_image.status_message = sm
      Image.save(add_image)

    # delegate work to superclass version of method
    return super().form_valid(form)

  def get_success_url(self) -> str: 
    #redirects the URL on success.
    profile = Profile.objects.get(pk=self.kwargs['pk'])
    return reverse('show_profile',kwargs={'pk':profile.pk})
  

class UpdateProfileView(UpdateView):
    form_class = UpdateProfileForm 
    template_name = "mini_fb/update_profile_form.html"
    model = Profile
  




