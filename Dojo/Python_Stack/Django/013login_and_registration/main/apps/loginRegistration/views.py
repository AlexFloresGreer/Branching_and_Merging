from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import User, validationManager
import bcrypt
# password = b"super secret password"
#CONTROLLER
#Create your views here.
def index(request):
    return render(request, 'loginRegistration/index.html')

def register(request):
    error = False
    if not validationManager().validateEmail(request, request.POST['email']):
        error = True
    if not validationManager().validateName(request, request.POST['first_name'], request.POST['last_name']):
        error = True
    if not validationManager().validatePassword(request, request.POST['password'], request.POST['password_confirmation']):
        error = True

    if not error:
        hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
        messages.success(request, 'You have successfully been registered!')
        return redirect('/success/'+request.POST['first_name'])
    else:
        return redirect('/')

def login(request):
    user = validationManager().validateLogin(request, request.POST['email'], request.POST['password'])
    if user[0]:
        return redirect('/success/'+user[1])
    else:
        return redirect('/')

def success(request, name):
    return render(request, 'loginRegistration/success.html', {'name':name})
