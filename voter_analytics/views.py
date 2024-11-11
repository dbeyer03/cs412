from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter
from django.db.models.query import QuerySet
from typing import Any
import datetime

# Create your views here.
class VoterListView(ListView):
  template_name = 'voter_analytics/voters.html'
  model = Voter
  context_object_name = 'voters'
  paginate_by = 100

  def get_context_data(self,**kwargs):
    context = super(VoterListView,self).get_context_data(**kwargs)
    context['birth_years'] = range(1917,datetime.datetime.now().year)
    return context

  def get_queryset(self) -> QuerySet[any]:
    qs = super().get_queryset()
    qs = Voter.objects.all()

    if 'voter_score' in self.request.GET:         
      voter_score = self.request.GET['voter_score']
      if voter_score: # not empty string:
        if voter_score != "None":
          qs = qs.filter(voter_score__icontains=voter_score)
    

    if 'party_affiliation' in self.request.GET:         
        party_affiliation = self.request.GET['party_affiliation']
        if party_affiliation: # not empty string:
          if party_affiliation != "None":
            qs = qs.filter(party_affiliation__icontains=party_affiliation)
    
    if 'min_birthday' in self.request.GET:         
        birth_date = self.request.GET['min_birthday']
        if birth_date: # not empty string:
          if birth_date != "None":
            birth_date = int(birth_date)
            qs = qs.filter(birth_date__gte=datetime.date(birth_date, 1, 1))
    
    if 'max_birthday' in self.request.GET:         
        birth_date = self.request.GET['max_birthday']
        if birth_date: # not empty string:
          if birth_date != "None":
            birth_date = int(birth_date)
            qs = qs.filter(birth_date__lte=datetime.date(birth_date, 12, 31))
    
    if 'v20state' in self.request.GET:
      v20state = self.request.GET['v20state']
      if v20state:
        qs = qs.filter(v20state__icontains="TRUE")

    if 'v21town' in self.request.GET:
      v21town = self.request.GET['v21town']
      if v21town:
        qs = qs.filter(v21town__icontains="TRUE")

    if 'v21primary' in self.request.GET:
      v21primary = self.request.GET['v21primary']
      if v21primary:
        qs = qs.filter(v21primary__icontains="TRUE")
    
    if 'v22general' in self.request.GET:
      v22general = self.request.GET['v22general']
      if v22general:
        qs = qs.filter(v22general__icontains="TRUE")
    
    if 'v23town' in self.request.GET:
      v23town = self.request.GET['v23town']
      if v23town:
        qs = qs.filter(v23town__icontains="TRUE")

  

    
    '''
    elif 'birth_date' in self.request.GET:         
        birth_date = self.request.GET['birth_date']
        if birth_date: # not empty string:
            qs = Result.objects.filter(birth_date__icontains=birth_date)
    
    elif 'voter_score' in self.request.GET:         
        voter_score = self.request.GET['voter_score']
        if voter_score: # not empty string:
            qs = Result.objects.filter(voter_score__icontains=voter_score)
    '''
    
    return qs

def list_years(request):

  template_name = "voter_analytics/voter_search.html"

  context = {
    'year_range': range(1917,2005)
  }

  return render(request,template_name,context)

class VoterDetailView(DetailView):
  model = Voter
  template_name = 'voter_analytics/voter_details.html'
  context_object_name = 'voter'

  

