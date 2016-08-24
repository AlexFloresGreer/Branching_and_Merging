from django.shortcuts import render, HttpResponse, redirect
from ..registration.models import User
from ..courses.models import Courses
from django.db.models import Count
from .models import Add_User

def index(request):
    # taken_courses = Courses.objects.filter(id=id)
    context={
        'users' : User.objects.all(),
        'courses':Courses.objects.all(),
    }


    return render(request, "integration/index.html", context)

def add_users(request):

    return render(request, "integration/index.html")
