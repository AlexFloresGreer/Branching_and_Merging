from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import User, validationManager, Book, Author, Reviews
import bcrypt
import datetime
# from datetime import datetime

#CONTROLLER
#Create your views here.
def index(request):
    return render(request, 'beltreview/index.html')

def register(request):
    error = False
    if not validationManager().validateEmail(request, request.POST['email']):
        error = True

    if not validationManager().validateName(request, request.POST['first_name'], request.POST['last_name']):
        error = True
#convert bday
    if not validationManager().validateBirthday(request, request.POST['birthday']):
        error = True

    if not validationManager().validatePassword(request, request.POST['password'], request.POST['password_confirmation']):
        error = True

    if not error:
        hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())
        user_info = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],birthday=request.POST['birthday'], password=hashed)
        user_info.save()
        messages.success(request, 'You have successfully been registered! Now you can login')
        return redirect('/')
    else:
        return redirect('/')

def login(request):
    user = validationManager().validateLogin(request, request.POST['email'], request.POST['password'])
    if user:
        request.session['user'] = request.POST['email']
        return redirect('/books')
    else:
        return redirect('/')

def books(request):
	return render(request,'beltreview/books.html')

def add(request):
    return render(request,'beltreview/add.html')

def showbookreview(request):
    return render(request, 'beltreview/showbookreview.html')

def showuser(request):
    return render(request, 'beltreview/showuser.html')


def logout(request):
	del request.session['user']
	return render(request,'beltreview/index.html')
