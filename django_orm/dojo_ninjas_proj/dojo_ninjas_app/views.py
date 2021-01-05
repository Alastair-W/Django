from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "dojo_list": Dojo.objects.all(),
    }
    return render(request, 'index.html', context)

def dojoForm(request):
    Dojo.objects.create(
        name=request.POST['name'], 
        city=request.POST['city'], 
        state=request.POST['state']
    )
    return redirect('/')



def ninjaForm(request):
    Ninja.objects.create(
        first_name=request.POST['fname'], 
        last_name=request.POST['lname'], 
        dojo=request.POST['dojo']
    )
    return redirect('/')