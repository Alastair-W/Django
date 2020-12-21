from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def results(request):
    if request.method == 'POST':
        context={
            'name': request.POST["name"],
            'location': request.POST["location"],
            'language': request.POST["language"],
            'comments': request.POST["comments"] 
        }
        print(request.POST)
        return render(request, 'results.html', context)

def about_page(request):
    return render(request, 'about.html')

# Create your views here.
