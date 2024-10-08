## quotes/urls.py
## description: URL patterns for the quotes app

from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from . import views

# all of the URLs that are part of this app
urlpatterns = [
  path(r'', views.quote, name="quote"),
  path(r'quote', views.quote, name="quote"),
  path(r'about', views.about, name="about"),
  path(r'show_all', views.show_all, name="show_all"),
]