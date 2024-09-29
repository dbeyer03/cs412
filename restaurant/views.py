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

  specials = {
    'special1': "Sour Patch Taco Deluxe",
    'special2': "Watercress Salad Topped With Nerds and Sweet Tarts",
    'special3': "Pixie-Stick Braised Pork",
    'special4': "Sweet and Cherry-Sour Soup",
  }

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
#      'taco':taco, 
#      'salad':salad,
#      'pork':pork,
#      'soup':soup,
#      'burger':burger,
#      'giro':giro,
#      'special':special,
#      'instructions':instructions,
    }
    total_price = 0

    if 'pork' in request.POST:
      context['pork'] = "pork"
      total_price += 16
    else:
      context['pork'] = "no-pork"

    if 'taco' in request.POST:
      context['taco'] = "taco"
      total_price += 8
    else:
      context['taco'] = "no-taco"
    
    if 'salad' in request.POST:
      context['salad'] = "salad"
      total_price += 13
    else:
      context['salad'] = "no-salad"

    if 'soup' in request.POST:
      context['soup'] = "soup"
      total_price += 14
    else:
      context['soup'] = "no-soup"
    
    if 'burger' in request.POST:
      context['burger'] = "burger"
      total_price += 9
    else:
      context['burger'] = "no-burger"
    
    if 'giro' in request.POST:
      context['giro'] = "giro"
      total_price += 12
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
    
    context['price'] = str(total_price)

    context['time'] = datetime.now()+timedelta(minutes=random.randrange(30,60))

    # +timedelta(minutes=random.randrange(30,60))

    return render(request,template_name, context)
  return redirect("order")