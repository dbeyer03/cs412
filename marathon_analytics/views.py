from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Result
from django.db.models.query import QuerySet
# Create your views here.

class ResultsListView(ListView):
  '''View to display list of marathon results.'''

  template_name = 'marathon_analytics/results.html'
  model = Result 
  context_object_name = "results"
  paginate_by = 50

  def get_queryset(self) -> QuerySet[any]:
    '''return the set of Results'''

    #use the superclass version of the queryset
    qs = super().get_queryset()

    if 'city' in self.request.GET:
      city = self.request.GET['city']
      qs = Result.objects.filter(city=city)

    return qs[:25]

class ResultsDetailView(DetailView):
  '''Whow the results for one record.'''

  template_name = 'marathon_analytics/result_detail.html'
  model = Result
  '''Using r means that we can do a lotta copy 'n pastin' here.'''
  context_object_name = 'r'