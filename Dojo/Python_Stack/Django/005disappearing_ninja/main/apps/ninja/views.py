from django.shortcuts import render, HttpResponse, redirect
from django.conf.urls import url

def none(request):
    context = {
        'id': "none",
    }
    return render(request, 'ninja/index.html', context)

def index(request):
    context = {
        'id': "ninjas",
    }
    return render(request, 'ninja/index.html', context)

def ninjas(request,id):
    context = {
        'id': id,
    }
    return render(request, 'ninja/index.html', context)