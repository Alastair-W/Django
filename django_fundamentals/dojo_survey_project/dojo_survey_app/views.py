from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def create_results(request):
    # if request.method == 'POST':
    print(request.POST)
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comments': request.POST['comments'] 
    }
    return redirect('/dojo_survey_app/display_results')         

def results(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'results.html', context)

def about_page(request):
    return render(request, 'about.html')

# Create your views here.
