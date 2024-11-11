from django.urls import path
from django.conf import settings
from . import views
from django.urls import path, include


# create a list of URLs for this app:
urlpatterns = [
    # map the URL to the view
    path('', views.ResultsListView.as_view(), name="home"),
    path('results', views.ResultsListView.as_view(), name="results"),
    path(r'result/<int:pk>', views.ResultDetailView.as_view(), name="result_detail"),

]