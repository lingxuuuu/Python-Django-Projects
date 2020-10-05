from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'name': request.POST['name'],
        'location' : ['San Jose', 'Seattle', 'Los Angeles', 'Austin'],
         
        'language' : ['Chinese', 'English', 'Spanish', 'French'],
        'comment': request.POST['comment'],
    }
    return render(request, 'index.html', context)

