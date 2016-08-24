from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import User, Poke, validationManager
import bcrypt
import datetime
# from datetime import datetime


# password = b"super secret password"
#CONTROLLER
#Create your views here.
def index(request):
    return render(request, 'caralibroapp/index.html')

def register(request):
    error = False
    if not validationManager().validateEmail(request, request.POST['email']):
        error = True

    if not validationManager().validateName(request, request.POST['first_name'], request.POST['alias']):
        error = True
#convert bday
    if not validationManager().validateBirthday(request, request.POST['birthday']):
        error = True

    if not validationManager().validatePassword(request, request.POST['password'], request.POST['password_confirmation']):
        error = True

    if not error:
        hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], alias=request.POST['alias'], email=request.POST['email'],birthday=request.POST['birthday'], password=hashed)
#session
        request.session['alias']=request.POST['alias']
        messages.success(request, 'You have successfully been registered!')
        return redirect('/pokes')
    else:
        return redirect('/')

def login(request):
    user = validationManager().validateLogin(request, request.POST['email'], request.POST['password'])
    print user
    if user:
        request.session['alias']=request.POST['alias']
        return redirect('/pokes')
    else:
        return redirect('/')

def pokes(request):
    context={
        'friends' : User.objects.exclude(alias=request.session['alias'])
        }
    return render(request, 'caralibroapp/pokes.html', context)

def total_pokes(request, id):
    # query="SELECT count(user_id) FROM user"
    return render(request, 'caralibroapp/pokes.html')



def logout(request):
    del request.session['alias']
    return redirect('/')
