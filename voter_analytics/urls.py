from django.urls import path
from django.conf import settings
from . import views
from django.urls import path, include


# create a list of URLs for this app:
urlpatterns = [
    # map the urls to the views.
    path('', views.VoterListView.as_view(), name="voters"),
    path('voters', views.VoterListView.as_view(), name="voters"),
    path('voter/<int:pk>', views.VoterDetailView.as_view(), name="voter"),
    path('graphs', views.GraphListView.as_view(), name="graphs"),

]