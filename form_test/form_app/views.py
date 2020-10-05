
from django.shortcuts import render, HttpResponse, redirect

def index(request):
   ## index is the route that shows the form
    return render(request, 'index.html')

def create_user(request):
   #create_user is the route process the form
    print('Got post info ....')
    print(request.POST) #access the full form
    print(request.POST['name']) #this is from html name = "name"
    print(request.POST['email']) #this is from html email = "email"
    context = {
        'name' : request.POST['name'],
    #name on template, which is the key      
        'email' : request.POST['email'],
    }
    #return render (request, 'show.html', context)
    return redirect("/success")

def success (request):
   #success is the page when people submitted the form
    return render(request,"success.html")

