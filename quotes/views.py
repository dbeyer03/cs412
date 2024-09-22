from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# Create your views here.

def pick_item(items):
  pardoned_q = random.choice(list(items.values()))

  return pardoned_q

def get_quote(request):
  '''
  The view for the main page, which will display
  one random quote on the HTML template of the same name.
  '''

  #this template will present the response 
  template_name = "quotes/quote.html"

  # a dictionary of quotes
  list_quotes = {
    'quote1' : "We weep for a bird's cry, but not for a fish's blood. Blessed are those with a voice.",
    'quote2' : "In one word I would say I worship dogs like people worship God. Dogs are my religion.",
    'quote3' : "Just because a movie is satisfactory doesn't means that the person who makes it is satisfactory. One can make a wonderful movie but still not be a wonderful person.",
    'quote4' : "Ultimately, the joy of watching films is not in their story or characters but in the touch of the director, so judging whether the director is competent or incompetent, extraordinary or mediocre, is something immediate. If you can't judge a film after 3 minutes, that increases the likelihood that it's a masterpiece.",
    'quote5' : "Blessed are those with a voice.",
    'quote6' : "Ruins; I like ruins; I like museums; I like fish; I like birds; I like water.",
  }

  # a dictionary of Mamoru Oshii photos.

  list_pics = {
    'img1': 'oshii1.jpg',
    'img2': 'oshii2.jpg',
    'img3': 'oshii3.jpg',
  }

  pick_quote = pick_item(list_quotes)
  pick_pic = pick_item(list_pics)

  new_dict = {}
  new_dict['the_quote'] = pick_quote
  new_dict['the_pic'] = pick_pic
  new_dict['current_time'] = time.ctime()

  return render(request,template_name, new_dict)

def show_about(request):
  '''
  The view for the about page, which displays 
  information about legendary anime director Mamoru
  Oshii.
  '''

  # this template will present the response
  template_name = "quotes/about.html"

  about_dict = {
    'current_time':time.ctime(),
  }

  return render(request, template_name, about_dict)

def all_items(request):
  '''
  The view for the page of all photos and quotes.
  '''

  # this template will present the response 
  template_name = "quotes/show_all.html"

  items_dict = {
    'current_time':time.ctime(),
    'quote1' : "We weep for a bird's cry, but not for a fish's blood. Blessed are those with a voice.",
    'quote2' : "In one word I would say I worship dogs like people worship God. Dogs are my religion.",
    'quote3' : "Just because a movie is satisfactory doesn't means that the person who makes it is satisfactory. One can make a wonderful movie but still not be a wonderful person.",
    'quote4' : "Ultimately, the joy of watching films is not in their story or characters but in the touch of the director, so judging whether the director is competent or incompetent, extraordinary or mediocre, is something immediate. If you can't judge a film after 3 minutes, that increases the likelihood that it's a masterpiece.",
    'quote5' : "Blessed are those with a voice.",
    'quote6' : "Ruins; I like ruins; I like museums; I like fish; I like birds; I like water.",
    'img1': 'oshii1.jpg',
    'img2': 'oshii2.jpg',
    'img3': 'oshii3.jpg',
  }

  return render(request, template_name, items_dict)