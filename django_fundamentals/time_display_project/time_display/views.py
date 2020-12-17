from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime

def index(request):
    now = datetime.now()
    context ={
        "timeA": strftime("%b %d, %Y", gmtime()),
        "timeB": strftime("%H:%M %p", gmtime()),
        "timeAltA": now.strftime("%B %d, %Y"),
        "timeAltB": now.strftime("%H:%M %p")
    }
    return render(request, 'index.html', context)
# Create your views here.
