from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
import random
import string


# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session[ 'count' ] = 0
    request.session['count'] += 1

    data = {
            "random_string" : ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(14)),

    }


    return render(request, 'random_word_generator/index.html', data)