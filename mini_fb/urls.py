

from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from . import views

# all of the URLs that are part of this app
urlpatterns = [
  path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
  path(r'show_all_profiles', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
  path(r'info', views.info_page, name="info"),
  path(r'profile/<int:pk>', views.ShowProfilePageView.as_view(), name="show_profile"), 
  path(r'create_profile_form', views.CreateProfileView.as_view(), name="create_profile_form"), 
]