## quotes/urls.py
## description: URL patterns for the quotes app

from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from . import views

# all of the URLs that are part of this app
urlpatterns = [
  path(r'', views.main, name="main"),
  path(r'order', views.order, name="order"),
  path(r'confirmation', views.confirmation, name="confirmation"),

]