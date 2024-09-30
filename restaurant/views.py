from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import time
import random
from datetime import timedelta, date, datetime

# Create your views here.
def pick_item(items):
  pardoned_q = random.choice(list(items.values()))

  return pardoned_q


def home_page_view(request):
  return HttpResponse("Homepage")

def main(request):
  template_name = "restaurant/main.html"

  context = {
    'current_time': time.ctime(),
  }

  return render(request,template_name,context)

def order(request):
  template_name = "restaurant/order.html"

  # The four special menu items.
  specials = {
    'special1': "Sour Patch Taco Deluxe",
    'special2': "Watercress Salad Topped With Nerds and Sweet Tarts",
    'special3': "Pixie-Stick Braised Pork",
    'special4': "Sweet and Cherry-Sour Soup",
  }

  #pick_item function used to pick random meal.
  daily_special = pick_item(specials)

  context = {
    'daily_special':daily_special,
  }

  return render(request,template_name, context)

def confirmation(request):
  template_name = "restaurant/confirmation.html"


  if request.POST:
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']

  
    context = {
      'current_time': time.ctime(),
      'name': name,
      'phone':phone,
      'email':email,
    }
    total_price = 0

    # checks which menu items were in the meal.
    # adds them to the context if selected.
    # Adds the prices to total_price.
    if 'pork' in request.POST:
      context['pork'] = "pork"
      total_price += 16
    else:
      context['pork'] = "no-pork"

    if 'taco' in request.POST:
      context['taco'] = "taco"
      total_price += 8

      # adds toppings if selected, but 
      # only if the dish was selected.
      if 'tacomato' in request.POST:
        context['tacomato']= "tomato"
      else:
        context['tacomato']= "no-tomato"

      if 'tacocheese' in request.POST:
        context['tacocheese']= "tacocheese"
      else:
        context['tacocheese']= "no-lettuce"

      if 'tacolettuce' in request.POST:
        context['tacolettuce']= "tacolettuce"
      else:
        context['tacolettuce']= "no-lettuce"

      if 'tacoskittles' in request.POST:
        context['tacoskittles']= "tacoskittles"
      else:
        context['tacoskittles']= "no-tacoskittles"

    else:
      context['taco'] = "no-taco"


    
    if 'salad' in request.POST:
      context['salad'] = "salad"
      total_price += 13

      if 'dressing' in request.POST:
        context['dressing'] = "dressing"
      else:
        context['dressing'] = "no-dressings"

      if 'craisins' in request.POST:
        context['craisins'] = "craisins"
      else:
        context['craisins'] = "no-craisins"

      if 'laffy_taffy' in request.POST:
        context['laffy_taffy'] = "laffy_taffy"
      else:
        context['laffy_taffy'] = "no_laffy_taffy"

    else:
      context['salad'] = "no-salad"

    if 'soup' in request.POST:
      context['soup'] = "soup"
      total_price += 14

      if 'spicypeppers' in request.POST:
        context['spicypeppers'] = "spicypeppers"
      else:
        context['spicypeppers'] = "nospice"

      if 'fruitgushers' in request.POST:
        context['fruitgushers'] = "fruitgushers"
      else:
        context['fruitgushers'] = "nogush"

    else:
      context['soup'] = "no-soup"
    
    if 'burger' in request.POST:
      context['burger'] = "burger"
      total_price += 9

      if 'burger_lettuce' in request.POST:
        context['burger_lettuce'] = "burger_lettuce"
      else:
        context['burger_lettuce'] = "no_burger_lettuce"

      if 'burger_cheese' in request.POST:
        context['burger_cheese'] = "burger_cheese"
      else:
        context['burger_cheese'] = "no_burger_cheese"
      
      if 'burger_kids' in request.POST:
        context['burger_kids'] = "burger_kids"
      else:
        context['burger_kids'] = "no_burger_kids"
    else:
      context['burger'] = "no-burger"
    
    if 'giro' in request.POST:
      context['giro'] = "giro"
      total_price += 12
      if 'feta' in request.POST:
        context['feta'] = "feta"
      else:
        context['feta'] = "no_feta"
      if 'ziki' in request.POST:
        context['ziki'] = "ziki"
      else:
        context['ziki'] = "no_ziki"
      if 'mike' in request.POST:
        context['mike'] = "mike"
      else:
        context['mike'] = "no_mike"
    else:
      context['giro'] = "no-giro"
    
    if 'daily_special' in request.POST:
      context['daily_special'] = request.POST['daily_special']
      total_price += 15
    else:
      context['daily_special'] = "no_special"
    
    if 'instructions' in request.POST:
      context['instructions'] = request.POST['instructions']
    else:
      context['instructions'] = "None."
    
    # stores the price as a variable.
    context['price'] = str(total_price)

    # stores random time 30-60 minutes from now.
    context['time'] = datetime.now()+timedelta(minutes=random.randrange(30,60))


    return render(request,template_name, context)
  return redirect("order")