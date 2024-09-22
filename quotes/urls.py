## quotes/urls.py
## description: URL patterns for the quotes app

from django.urls import path
from django.conf import settings
from . import views

# all of the URLs that are part of this app
urlpatterns = [
  path(r'', views.get_quote, name="quote"),
  path(r'about', views.show_about, name="about"),
  path(r'show_all', views.all_items, name="show_all"),

]