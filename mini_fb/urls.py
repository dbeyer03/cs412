

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
  path(r'create_profile', views.CreateProfileView.as_view(), name="create_profile_form"), 
  path(r'profile/<int:pk>/create_status', views.CreateStatusMessageView.as_view(), name="create_status_form"), 
  path(r'profile/<int:pk>/update', views.UpdateProfileView.as_view(), name="update_profile"),
  path(r'status/<int:pk>/delete', views.DeleteStatusMessageView.as_view(), name='delete_status_form'),
  path(r'status/<int:pk>/update', views.UpdateStatusMessageView.as_view(), name='update_status_form'),
  path(r'profile/<int:pk>/add_friend/<int:other_pk>', views.CreateFriendView.as_view(), name='add_friend'),
  path(r'profile/<int:pk>/friend_suggestions', views.ShowFriendSuggestionsView.as_view(), name='friend_suggestions')
]