from django.shortcuts import render, redirect
import random
from datetime import datetime

gold_building = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (-50,50)
}


# Create your views here.
def index(request):
    if not "activities" in request.session or "gold" not in request.session:
        request.session['activities'] = []
        request.session['gold'] = 0
    return render(request, 'index.html')

def farm_gold(request):
    # set the time in the right format
    currentTime = datetime.now()
    timestamp = currentTime.strftime("%Y/%m/%d %I:%M%p")
    # retrieve the gold earn range from the building_type dictionary ising the value passed from the form
    building_type = request.POST['building']
    print(building_type)
    # if building_type is casino money can be lost or earned
    if building_type == 'casino':
        building_details = gold_building[building_type]
        gold_num = random.randint(building_details[0], building_details[1])
        if gold_num < 0:
            message = f"Unlucky, you lost {gold_num} at the {building_type} on {timestamp}"
            result = 'lose'
        else:
            message = f"Sweet, you won {gold_num} at the {building_type} on {timestamp}"
            result = 'earn'
    else:
        building_details = gold_building[building_type]
        gold_num = random.randint(building_details[0], building_details[1])
        message = f"Sweet, you earned {gold_num} at the {building_type} on {timestamp}"
        result = 'earn'
    
    request.session['gold'] += gold_num
    request.session['activities'].append({"message": message, "result": result})
    
    print(request.session['activities'])
    return redirect('/')

def refresh(request):
    request.session.flush()
    return redirect('/')