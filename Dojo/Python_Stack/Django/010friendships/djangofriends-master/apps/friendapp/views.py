from django.shortcuts import render
from .models import Friendships, Users

# Create your views here.
#1
# from . import models
# def index(req):
#     users = models.Users.objects.all()
#     context = {'users':users}
#     return render(req, "friendapp/index.html",context)
# ]
#2
# from .models import Friendships, Users
# def index(req): #this will print all the friendship objects to terminal
#     friendships = Friendships.objects.all()
#     context = {
#         'friendships' : friendships
#     }
#     print friendships #print friendships.query
#     return render(req, "friendapp/index.html", context)

#3 Pass the result from 2 to the index.html
    # page using context and print out the friend.first_name,
    # friend.last_name from each of these objects.


def index(req):
    users = Users.objects.all()
    friendships = Friendships.objects.filter(user__first_name='Ava', user__last_name ='Rodriguez')
    context ={
        'friendships': friendships,

    }
    return render(req, "friendapp/index.html", context)











