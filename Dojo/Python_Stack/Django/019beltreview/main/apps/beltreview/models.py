from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
from datetime import datetime
import bcrypt
Email_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class validationManager(models.Manager):
    def validateEmail(self, request, email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]*$')
        if not EMAIL_REGEX.match(email):
            messages.error(request, "Email is not valid")
            return False
        else:
            # check if email is already in database
            try:
                User.objects.get(email=email)
                messages.error(request, "Email is already in use")
                return False
            except User.DoesNotExist:
                pass
        return True

    def validateName(self, request, first_name, last_name):
        no_error = True
        if len(first_name) < 2 or any(char.isdigit() for char in first_name):
            messages.error(request, 'Frist name must be 2 characters and only letters')
            no_error = False
        if len(last_name) < 2 or any(char.isdigit() for char in last_name):
            messages.error(request, 'Last name must be 2 characters and only letters')
            no_error = False
        return no_error

    def validateBirthday(self, request, birthday):
        no_error = True
        now = strftime('%Y-%m-%d')
        if request.POST['birthday'] == "":
            messages.error(request, 'Birthday can not be blank')
            no_error = False
        print now
        print request.POST['birthday']
        print now
        if request.POST['birthday'] > now:
            messages.error(request, 'Birthday can not be in the future')
            no_error = False
        return no_error
        
    def validatePassword(self, request, password, confirm_password):
        no_error = True
        if len(password) < 8:
            messages.error(request, 'Password must be greater than 8 characters')
            no_error = False
        if not password == confirm_password:
            messages.error(request, 'Password confirmation must match password')
            no_error = False
        return no_error

    def validateLogin(self, request, email, password):
        try:
            user = User.objects.get(email=email)
            if bcrypt.hashpw(password.encode('utf-8'), user.password.encode('utf-8')) == user.password:
                messages.success(request, "You've been logged in!")
                return (True, user.first_name)
        except User.DoesNotExist:
            messages.error(request, "Invalid email")
            return False



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField(null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    emailManager = validationManager()
    objects = models.Manager()

class Book(models.Model):
    title = models.CharField(max_length=45)
    author = models.ForeignKey('Author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# class ReviewManager(models.Model):
#     def create_review(self,form_data,user_id):
#         Try:
#

class Reviews(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey('User')
    book = models.ForeignKey('Book', default=1)
    # object = ReviewManager()
