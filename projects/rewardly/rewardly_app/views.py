from django.shortcuts import render, redirect
from .forms import *
from .models import *
from datetime import datetime

# Create your views here.

# GET
def index(request):
    return render(request, 'index.html')

def registerPage(request):
    get_form = RegistrationForm()
    print(f'Form is bound: {get_form.is_bound}')
    context = {
        'form': get_form
    }
    return render(request, 'registerPage.html', context)

def authenticate(request):
    if request.session['user_id']:
        user = User.objects.get(id=request.session['user_id']) 
        allCC = user.credit_card.all().count()
        allR = user.retailer.all().count()
        context = {
            'user': user,
            'allCC': allCC,
            'allR': allR,
            'regDate': user.created_at.strftime("%b %d %Y") 
        }
        return render(request, 'profile.html', context)

def logOut(request):
    request.session.flush()
    return redirect('/')

def creditCards(request):
    if request.session['user_id']:
        user = User.objects.get(id=request.session['user_id']) 
        allCC = Credit_card.objects.all()
        context = {
            'user': user,
            'allCC': allCC
        }
        return render(request, 'creditCards.html', context)
    
    else:
        return redirect('/')

def retailers(request):
    if request.session['user_id']:
        user = User.objects.get(id=request.session['user_id']) 
        allR = Retailer.objects.all()
        context = {
            'user': user,
            'allR': allR
        }
        return render(request, 'retailers.html', context)
    
    else:
        return redirect('/')

def displayCC(request, ccID):
    if request.session['user_id']:
        user = User.objects.get(id=request.session['user_id']) 
        ccSelect = Credit_card.objects.get(id=ccID)
        allRetailers = Reward.objects.filter(credit_card=ccSelect).order_by('-points')
        context = {
            'user': user,
            'ccSelect': ccSelect,
            'allRetailers': allRetailers
        }
        return render(request, 'ccSelect.html', context)

def favorite(request, ccID):
    if request.session['user_id']:
        curr_user = User.objects.get(id=request.session['user_id'])
        curr_cc = Credit_card.objects.get(id=ccID)
        if curr_user in curr_cc.user.all():
            curr_user.credit_card.remove(curr_cc)
        else:
            curr_user.credit_card.add(curr_cc)
        return redirect(f'/displayCC/{ ccID }')
    else:
        return render('/registerPage')

def favoriteRetail(request, retailID):
    curr_user = User.objects.get(id=request.session['user_id'])
    curr_retail = Retailer.objects.get(id=retailID)
    if curr_user in curr_retail.user.all():
        curr_user.retailer.remove(curr_retail)
    else:
        curr_user.retailer.add(curr_retail)
    return redirect(f'/retailers')


def seeFavorites(request):
    if request.session['user_id']:
        curr_user = User.objects.get(id=request.session['user_id'])
        favRetail = Retailer.objects.filter(user=curr_user)
        favCC = Credit_card.objects.filter(user=curr_user)
        comboList = []
        retailList = []
        for item in favRetail:
            retailList.append(item.retail_name)
            for cc in Reward.objects.filter(retailer=item):
                comboList.append([item.retail_name, cc.credit_card.cc_name, cc.points])
        
        context = {
            'comboList': comboList,
            'retailList': retailList,
            'favCC': favCC
        }
        return render(request, 'seeFavorites.html', context)
    else:
        return redirect('/registerPage')

# POST

def signUp(request):
    if request.method == 'POST':
        # Bind the POST data to an instance of our RegisterForm
        post_form = RegistrationForm(request.POST)
        print(f'Form is bound: {post_form.is_bound}')
        # Now test that bound_form using built-in methods!
        # *************************
        print(f'Form is valid: {post_form.is_valid()}') # True or False, based on the validations that were set!
        if post_form.is_valid():
            print(f'Validated form data: {post_form.cleaned_data}')
            hashpwd = bcrypt.hashpw(post_form.cleaned_data['password'].encode(), bcrypt.gensalt()).decode()
            User.objects.create(
                first_name = post_form.cleaned_data['first_name'],
                last_name = post_form.cleaned_data['last_name'],
                email = post_form.cleaned_data['email'],
                password = hashpwd
            )
            request.session['valid'] = post_form.is_valid()
            user = User.objects.get(email=post_form.cleaned_data['email'])
            request.session['user_id'] = user.id
            return redirect('/authenticate')
        else:
            context = {
                'form': post_form,
                'form_errors': post_form.errors
            }
            return render(request, 'registerPage.html', context)

def logIn(request):
    if request.method == 'GET':
        return redirect('/registerPage')
    # errors = User.objects.validateLogin(request.POST)
    # if errors:
    #     for error in errors:
    #         messages.error(request, errors[error])
    #     return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/authenticate')

