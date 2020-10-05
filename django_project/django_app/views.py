from django.shortcuts import render, HttpResponse, redirect ## add redirect to import statement

def index_main(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render (request, "index.html", context)

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def root(request):
    return redirect("/blogs")

def new (request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, number=66):
    return HttpResponse(f'placeholder to display blog number: {number}')

def edit(request, number=66):
    return HttpResponse(f'placeholder to edit blog {number}')

def destroy(request, number = 66):
    return redirect('/blogs')

def json(request):
    pass