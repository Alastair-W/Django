from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def word_gen(request):
    return render(request, 'word_gen_page.html')

def run_word_gen(request):
    unique_id = get_random_string(length=14)
    request.session['word'] = unique_id
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return redirect('/random_word')

def reset(request):
    request.session.flush()
    return redirect('/random_word')
# Create your views here.

