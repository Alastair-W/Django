from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'formtest/index.html')

def register(request):
    # Confirm that the HTTP verb was a GET
    if request.method == 'POST':
        # Bind the POST data to an instance of our RegisterForm
        post_form = RegistrationForm(request.POST)
        request.session['valid'] = post_form.is_valid()
        request.session['clean'] = post_form.cleaned_data
        request.session['errors'] = post_form.errors
        print(f'Form is bound: {post_form.is_bound}')
        # Now test that bound_form using built-in methods!
        # *************************
        print(f'Form is valid: {post_form.is_valid()}') # True or False, based on the validations that were set!
        if post_form.is_valid():
            print(f'Validated form data: {post_form.cleaned_data}')
            print(f'Validated form errors: {post_form.errors}')
        else:
            print(f'Validated form data: {post_form.cleaned_data}')
            print(f'Validated form errors: {post_form.errors}') # Any errors in this form as a dictionary 
        print(request.session['clean'])
        # *************************
        return redirect('/secure')
    else:
        get_form = RegistrationForm()
        print(f'Form is bound: {get_form.is_bound}')
        context = {
            'form': get_form
        }
    return render(request, 'formtest/register.html', context)

def secure(request):
    return render(request, 'formtest/secure.html')

        