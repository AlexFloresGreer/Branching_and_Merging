from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import warnings
import bcrypt
import re
from datetime import datetime

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def isValid(self, userInfo, request):
        noError = True
#registration
        if len(userInfo['first_name']) < 2:
            messages.warning(request, "First Name must be greater than 2 characters")
            noError = False
        if len(userInfo['last_name']) < 2:
            messages.warning(request, "Last Name must be greater than 2 characters")
            noError = False
        if not userInfo['first_name'].isalpha():
            messages.warning(request, "First name cannot be other than alphabetic characters")
            noError = False
        if not userInfo['last_name'].isalpha():
            messages.warning(request, "Last name cannot be other than alphabetic characters")
            noError = False
        if len(userInfo['email']) < 1:
            messages.warning(request, "Email cannot be blank!")
            noError = False
        if not EMAIL_REGEX.match(userInfo['email']):
            messages.warning(request, "Invalid Email Address!")
            noError = False
        if len(userInfo['password']) < 7:
            messages.warning(request, "Pasword should be more than 7 characters!")
            noError = False
        if userInfo['password'] != userInfo['confirm_password']:
            messages.warning(request, "Passwords don't match!")
            noError = False
        if User.objects.filter(email = userInfo['email']):
            messages.error(request, "Email already exists!")
            noError = False
        if noError == True:
            print "welcome" * 5
            messages.success(request, "Success! Welcome, " + userInfo['first_name'] + "!")
            hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name = userInfo['first_name'], last_name = userInfo['last_name'], email = userInfo['email'], password = hashed, birthdate=userInfo['birthdate'])
        return noError

#login
    def ExistedUserLogin(self, userInfo, request):
        noError = True
        if User.objects.filter(email = userInfo['email']):
            hashed = User.objects.get(email = userInfo['email']).password
            hashed = hashed.encode('utf-8')
            password = userInfo['password']
            password = password.encode('utf-8')
            if bcrypt.hashpw(password, hashed) == hashed:
                messages.success(request, "Success! Welcome, " + User.objects.get(email = userInfo['email']).first_name + "!")
                noError = True
            else:
                messages.warning(request, "Fail to login. Incorrect password.")
                noError = False
        else:
            messages.warning(request, "Fail to login. Incorrect email.")
            noError = False
        return noError



class User(models.Model):
    userManager = UserManager()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    birthdate = models.DateField(blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = models.Manager()
