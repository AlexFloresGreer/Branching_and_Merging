from django.shortcuts import render, HttpResponse, redirect
from django.conf.urls import url


def index(request):
    context = {
        'email': "blog@gmail.com",
        'name': "mike"
    }
    return render(request, 'passing_variables/index.html',context )

def show(request, id):
    context = {
        'id': "id",
    }
    return render(request, 'passing_variables/show.html',context )
