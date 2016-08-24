from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, UserManager
import warnings
import datetime

#landing page
def index(request):
    return render(request, "registration/index.html")

#registration
def process(request):
    if User.userManager.isValid(request.POST, request):
        error = False
        return HttpResponseRedirect(reverse('success'))
    else:
        error = True
        return HttpResponseRedirect(reverse('index'))

def success(request):
    return render(request, "registration/success.html")

#login
def login(request):
    if User.userManager.ExistedUserLogin(request.POST, request):
        error = False
        return HttpResponseRedirect(reverse('success'))
    else:
        error = True
        return HttpResponseRedirect(reverse('index'))

#logout
def logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('index'))
