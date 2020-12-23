from django.shortcuts import render

# Create your views here.
def home_screen(requests):
    return render(requests, 'home.html')