from django.shortcuts import render, HttpResponse, redirect
#import random

def index(request):
    # random
    if 'counter' in request.session:
        print('Counter exists')
        request.session['counter'] += 1
        
    else:
        print('key Counter does Not exists')
        request.session['counter'] = 1
        
    return render(request, 'index.html')


def destroy(request):
    del request.session['counter']
    return redirect('/')

