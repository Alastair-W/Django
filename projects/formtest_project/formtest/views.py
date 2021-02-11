from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
import bcrypt
from django.contrib.auth import authenticate, login
from datetime import datetime

# Create your views here.
#GET

def index(request):
    return render(request, 'formtest/index.html')


def secure(request):
    if request.session['user_id']:
        user = User.objects.get(id=request.session['user_id'])
        now = datetime.now()
        if now.strftime("%b %d %Y %H:%M") == user.created_at.strftime("%b %d %Y %H:%M"):
            regStatus = True
        else:
            regStatus = False 
            context = {
                'user': user,
                'regStatus': regStatus,
                'regDate': user.created_at.strftime("%b %d %Y")
            }
        return render(request, 'formtest/profile.html', context)

def retailers(request):
    return render(request, 'formtest/retailers.html')

def creditCards(request):
    allCC = Credit_card.objects.all()
    curr_user = User.objects.get(id=request.session['user_id'])
    allP = Program.objects.all()
    context = {
        'allCC': allCC,
        'curr_user': curr_user,
        'allP': allP
    }
    return render(request, 'formtest/creditcards.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def loginPage(request):
    return render(request, 'formtest/login.html')

def navigate(request):
    user = User.objects.get(id=request.session['user_id'])
    now = datetime.now()
    if now.strftime("%b %d %Y %H:%M") == user.created_at.strftime("%b %d %Y %H:%M"):
        regStatus = True
    else:
        regStatus = False 
        context = {
            'user': user,
            'regStatus': regStatus,
            'regDate': user.created_at.strftime("%b %d %Y")
        }
    return render(request, 'formtest/navHome.html', context)

#POST

def register(request):
    # Confirm that the HTTP verb was a GET
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
            return redirect('/secure')
        else:
            context = {
                'form': post_form,
                'form_errors': post_form.errors
            }
            return render(request, 'formtest/register.html', context)
        #     print(f'Validated form data: {post_form.cleaned_data}')
        #     print(f'Validated form errors: {post_form.errors}') # Any errors in this form as a dictionary 
        # *************************
    else:
        get_form = RegistrationForm()
        print(f'Form is bound: {get_form.is_bound}')
        context = {
            'form': get_form
        }

        return render(request, 'formtest/register.html', context)


def userLogin(request):
    if request.method == 'GET':
        return redirect('/loginPage')
    errors = User.objects.validateLogin(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/secure')


def favorite(request, cc_ID):
    if not request.session['user_id']:
        return redirect('/')
    if request.method == 'POST':
        curr_user = User.objects.get(id=request.session['user_id'])
        cc = Credit_card.objects.get(id=cc_ID)
        if curr_user in cc.user.all():
            curr_user.credit_card.remove(cc)
        else:
            curr_user.credit_card.add(cc)
        context = {
            'curr_user': curr_user
        }
        return render(request, 'formtest/ajax_fav.html', context)
        # return redirect('/creditCards')

def favProfile(request, cc_ID):
    if not request.session['user_id']:
        return redirect('/')
    curr_user = User.objects.get(id=request.session['user_id'])
    cc = Credit_card.objects.get(id=cc_ID)
    if curr_user in cc.user.all():
        curr_user.credit_card.remove(cc)
    else:
        curr_user.credit_card.add(cc)
    return redirect('/secure')