from django.shortcuts import render, HttpResponse, redirect

from datetime import datetime

from time import strftime
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'action' not in request.session:
        request.session['actions'] = []
    return render(request, 'index.html')

def add_money(request):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(request.POST)
    #check the bd
    if request.POST['building'] == 'farm':
        #generate a random number
        request.session['num'] = random.randint(10,20)
        #add the golds to session
        request.session['gold'] += request.session['num']
        #add activity to activities
        request.session['actions'].append(f"Earned {request.session['num']} golds from the farm! ({current_time})")

    
    if request.POST['building'] == 'cave':
        request.session['num'] = random.randint(5,10)
        request.session['gold'] += request.session['num']
        request.session['actions'].append(f"Earned {request.session['num']} golds from the cave! ({current_time})" )

    if request.POST['building'] == 'house':
        request.session['num'] = random.randint(2,5)
        request.session['gold'] += request.session['num']
        request.session['actions'].append(f"Earned {request.session['num']} golds from the house! ({current_time})" )

    if request.POST['building'] == 'casino':
        request.session['num'] = random.randint(-50,50)
        if request.session['num'] < 0:
            request.session['gold'] += request.session['num']
            request.session['actions'].append(f"Entered a casino and lost {request.session['num']} golds...Ouch ({current_time})" )
        if request.session['num'] >0:
            request.session['gold'] += request.session['num']
            request.session['actions'].append(f"Earned {request.session['num']} golds from the casino! ({current_time})")
    
    return redirect('/my_gold')

def my_gold (request):
    return render (request, 'index.html')

def reset (request):
    request.session.flush()
    return redirect('/')