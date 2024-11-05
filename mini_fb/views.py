from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import time
import random
from datetime import timedelta, date, datetime
from . models import *
from . forms import *
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse ## NEW
from .forms import UpdateProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

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

class CreateRegisterUserView(CreateView):
  form_class = UserCreationForm
  template_name = 'mini_fb/register.html'

  def dispatch(self, *args, **kwargs):

    if self.request.POST:
      print(f"self.request.POST={self.request.POST}")
      # reconstruct the UserCreationForm from the HTTP POST
      form = UserCreationForm(self.request.POST)

      if not form.is_valid():
        print(f'form.errors={form.errors}')
        # let's the CreateView superclass handle this problem!
        return super().dispatch(*args, **kwargs)

        # save the new User object
      user = form.save() # creates a new instance of User object in the database
      print(f"CreateRegisterUserView.dispatch: created user {user}")

      # log in the User
      login(self.request, user)
      print(f"CreateRegisterUserView.dispatch, user {user} is logged in.")

      return redirect(reverse('create_profile'))
    
    # let the superclass CreateView handle the HTTP GET request:
    return super().dispatch(*args, **kwargs)

class CreateProfileView(CreateView):
  '''A view to create a new profile page.'''
  form_class = CreateProfileForm
  template_name = 'mini_fb/create_profile_form.html'

  def get_context_data(self, **kwargs: any) -> dict[str,any]:
    # identify profile by its kwargs.
    context = super().get_context_data(**kwargs)
    register_form = UserCreationForm()
    context['register_form'] = register_form
    return context
  
  def form_valid(self,form):

    print(f'CreateProfileView.form_valid(): form={form.cleaned_data}')
    print(f'CreateProfileView.form_valid(): self.kwargs={self.kwargs}')

    # we handle the HTTP POST request
    # reconstruct the UserCreationForm from the HTTP POST
    form = UserCreationForm(self.request.POST)

    # save the new User object
    user = form.save() # creates a new instance of User object in the database

    # Attach user
    form.instance.user = user

    return super().form_valid(form)          



class CreateStatusMessageView(LoginRequiredMixin, CreateView):
  '''A view to create a status message on a profile page.'''
  form_class = CreateStatusMessageForm 
  template_name = 'mini_fb/create_status_form.html'

  def get_context_data(self, **kwargs: any) -> dict[str,any]:

    # identify profile by its kwargs.
    context = super().get_context_data(**kwargs)
    profile = Profile.objects.get(user=self.request.user)
    # store kwargs info in dictionary.
    context['profile'] = profile 

    return context

  def form_valid(self,form):

    print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
    print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

    # find the user who is logged in
    user = self.request.user

    # attach that user as a FK to the new Article instance
    form.instance.user = user

    # find the Profile indicated by the PK from the url pattern.
    profile = Profile.objects.get(user=self.request.user)

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
    profile = Profile.objects.get(user=self.request.user)
    return reverse('show_profile',kwargs={'pk':profile.pk})
  

class UpdateProfileView(LoginRequiredMixin, UpdateView):
  form_class = UpdateProfileForm 
  template_name = "mini_fb/update_profile_form.html"
  model = Profile

  def form_valid(self, form):
    '''
    Handle the form submission to update a Profile object.
    '''
    print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')

    # find the user who is logged in
    user = self.request.user

    # attach that user as a FK to the new Article instance
    form.instance.profile = user

    return super().form_valid(form)
  
  #return Profile corresponding to current user.
  def get_object(self):
    profile = Profile.objects.get(user=self.request.user)
    return profile

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
  template_name = "mini_fb/delete_status_form.html"
  model = StatusMessage 
  context_object_name = 'status'

  def get_success_url(self):
    '''Return a the URL to which we should be directed after the delete.'''
    # get the pk for this status message
    pk = self.kwargs.get('pk')
    status = StatusMessage.objects.filter(pk=pk).first() # get one object from QuerySet
    
    # find the proile to which this Status Message is related by FK
    profile = status.profile

    # find user for which the profile belongs to.
    user = profile.user
    
    #if (self.request.user is not None) and (self.request.user != user):

    # reverse to show the article page
    return reverse('show_profile', kwargs={'pk':profile.pk})


class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
  form_class = UpdateStatusMessageForm
  template_name = "mini_fb/update_status_form.html"
  model = StatusMessage
  context_object_name = 'status'

  def form_valid(self, form):
    '''
    Handle the form submission to update a StatusMessage object.
    '''
    print(f'UpdateStatusMessageView: form.cleaned_data={form.cleaned_data}')

    # find the user who is logged in
    user = self.request.user

    # attach that user as a FK to the new Article instance
    form.instance.user = user

    return super().form_valid(form)

  def get_success_url(self):
    '''Return a the URL to which we should be directed after the delete.'''
    # get the pk for this status message
    pk = self.kwargs.get('pk')
    status = StatusMessage.objects.filter(pk=pk).first() # get one object from QuerySet
    
    # find the proile to which this Status Message is related by FK
    profile = status.profile
    
    # reverse to show the article page
    return reverse('show_profile', kwargs={'pk':profile.pk})


class CreateFriendView(LoginRequiredMixin, View):
  #template_name = "mini_fb/add_friend.html"

  def dispatch(self, request, *args, **kwargs):

    # read URL parameters
    other_pk = self.kwargs.get('other_pk')

    # use object manager to find requisite Profile objects
    profile1 = Profile.objects.get(user=self.request.user)
    profile2 = Profile.objects.filter(pk=self.kwargs.get('other_pk')).first()


    Profile.add_friend(profile1, profile2)

    #redirect user back to profile page
    return redirect(reverse('show_profile', kwargs={'pk':profile1.pk}))
  
  #return Profile corresponding to current user.
  def get_object(self):
    profile = Profile.objects.get(user=self.request.user)
    return profile



class ShowFriendSuggestionsView(LoginRequiredMixin, DetailView):
  '''Show the suggested friends for a profile.'''
  model = Profile 
  template_name = 'mini_fb/friend_suggestions.html'
  context_object_name = 'profile'

  #return Profile corresponding to current user.
  def get_object(self):
    profile = Profile.objects.get(user=self.request.user)
    return profile

class ShowNewsFeedView(LoginRequiredMixin, DetailView):
  model = Profile 
  template_name = 'mini_fb/news_feed.html'
  context_object_name = 'profile'

  #return Profile corresponding to current user.
  def get_object(self):
    profile = Profile.objects.get(user=self.request.user)
    return profile