from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Voter
from django.db.models.query import QuerySet
from typing import Any
import datetime
import math
import plotly
import plotly.graph_objs as go

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

class GraphListView(ListView):
  template_name = 'voter_analytics/graphs.html'
  model = Voter
  context_object_name = 'voter'


  def get_context_data(self, **kwargs):
    '''
    Provide context variables for use in template
    '''
    # start with superclass context
    context = super().get_context_data(**kwargs)
    voter = context['voter']
    context['birth_years'] = range(1917,datetime.datetime.now().year)
    updated_query = self.get_queryset()
    num_voters = str(len(updated_query))

    # Create a pie chart of the distribution of voters by their party affiliation.

    # The labels.
    party_x = ['U','D','R','CC','L','T','O','G','J','Q','FF']

    # The values.
    all_u = updated_query.filter(party_affiliation__icontains='U')
    get_u = len(all_u)
    all_democrats = updated_query.filter(party_affiliation__icontains='D')
    get_d = len(all_democrats)
    all_republicans = updated_query.filter(party_affiliation__icontains='R')
    get_r = len(all_republicans)
    all_cc = updated_query.filter(party_affiliation__icontains='CC')
    get_cc = len(all_cc)
    all_l = updated_query.filter(party_affiliation__icontains='L')
    get_l = len(all_l)
    all_t = updated_query.filter(party_affiliation__icontains='T')
    get_t = len(all_t)
    all_o = updated_query.filter(party_affiliation__icontains='O')
    get_o = len(all_o)
    all_g = updated_query.filter(party_affiliation__icontains='G')
    get_g = len(all_g)
    all_j = updated_query.filter(party_affiliation__icontains='J')
    get_j = len(all_j)
    all_q = updated_query.filter(party_affiliation__icontains='Q')
    get_q = len(all_q)
    all_ff = updated_query.filter(party_affiliation__icontains='FF')
    get_ff = len(all_ff)

    # The list of values.
    party_y = [get_u,get_d,get_r,get_cc,get_l,get_t,get_o,get_g,get_j,get_q,get_ff]
    
    # generate the Pie chart
    fig1 = go.Pie(labels=party_x, values=party_y) 
    fig1_title = f"Voter distribution by Party Affiliation (n="+num_voters+")"
    # obtain the graph as an HTML div"
    voter_distribution = plotly.offline.plot({"data": [fig1], 
                                      "layout_title_text": fig1_title,
                                      }, 
                                      auto_open=False, 
                                      output_type="div")
    
    # Create a bar chart (histogram) illustration distribution of Voters by their years of birth.

    
    histogram_x = [str(x) for x in range(1917,2010)]
    histogram_y = [len(updated_query.filter(birth_date__icontains=x)) for x in histogram_x]
    fig2 = go.Bar(x=histogram_x, y=histogram_y)
    fig2_title = f"Voter distribution by Year of Birth (n="+num_voters+")"
    birthdays = plotly.offline.plot({"data": [fig2], 
                                      "layout_title_text": fig2_title,
                                      }, 
                                      auto_open=False, 
                                      output_type="div")
    
    #the information for the bar chart illustrating how many people voted per election.
    participation_x = ['v20state','v21town','v21primary','v22general','v23town']

    v20state_num = len(updated_query.filter(v20state__icontains="TRUE"))
    v21town_num = len(updated_query.filter(v21town__icontains="TRUE"))
    v21primary_num = len(updated_query.filter(v21primary__icontains="TRUE"))
    v22general_num = len(updated_query.filter(v22general__icontains="TRUE"))
    v23town_num = len(updated_query.filter(v23town__icontains="TRUE"))

    #used for number in title.
    v_total = str(v20state_num+v21town_num+v21primary_num+v22general_num+v23town_num)

    participation_y = [v20state_num,v21town_num,v21primary_num,v22general_num,v23town_num]

    fig3 = go.Bar(x=participation_x, y=participation_y)
    fig3_title = f"Voter distribution by Participation In Each Election (n="+num_voters+")"

    participation_graph = plotly.offline.plot({"data": [fig3], 
                                      "layout_title_text": fig3_title,
                                      }, 
                                      auto_open=False, 
                                      output_type="div")
    
    # Store all of the charts in context.
    context['voter_distribution'] = voter_distribution
    context['birthdays'] = birthdays
    context['participation_graph'] = participation_graph

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

    
    return qs




  

