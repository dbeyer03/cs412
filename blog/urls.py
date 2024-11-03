## blog/urls.py
## description: the app-specific URLS for the blog application

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for this app:
urlpatterns = [
    # path(url, view, name)
    path(r'', views.RandomArticleView.as_view(), name="random"), 
    path(r'show_all_buh', views.ShowAllView.as_view(), name="show_all_buh"), 

    #authentication URLs:
    # path('login/', auth_views.LoginView.as_view(), template_name='blog/login.html', name='login'),
]