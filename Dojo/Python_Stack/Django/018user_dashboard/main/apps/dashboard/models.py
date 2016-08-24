from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import re
from datetime import datetime
import bcrypt
Email_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def first_name(self,first_name):
    	if not len(first_name) > 2:
    		return(False,"Invalid Firstname")
    	else:
    		return(True,first_name)
    def first_name_charcheck(self,first_name):
    	if not first_name.isalpha():
    		return(False,"Invalid characters")
    	else:
    		return(True,first_name)
    def last_name(self,last_name):
    	if not len(last_name) > 2:
    		return(False,"Invalid lastname")
    	else:
    		return(True,last_name)
    def reg_email(self,email):
    	if not Email_REGEX.match(email):
    		return(False,"Invalid email")
    	else:
    		return(True,email)
    def birthday(self,birthday):
    	bday = birthday
    	now = datetime.now()
    	print now
    	if bday == "":
    		return(False, "Invalid Birthdate")
    	else:
    		return(True, birthday)
        bday_test = datetime.strptime(birthday, '%Y-%m-%d')
    def password(self,password):
    	if not len(password) > 4:
    		return(False,"Invalid password")
    	else:
    		password = password.encode()
    		hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    		return (True, hashed)
    def confirm_password(self,password,confirm_password):
    	if  password != confirm_password:
    		return(False,"confirm password")
    	else:
    		return(True,"password confirmed")
    def log(self,email,password):
    	try:
    	    user = self.get(email = email)
    	    print user.password
    	except:
    		return (False, "User Does not Exist")
    	password = password.encode()
    	user_password = user.password.encode()
    	if user and bcrypt.hashpw(password, user_password) == user_password:
    		return (True, user.first_name)
    	else:
    		return (False, "Password doesnot match")

        # def user_level(self, id):
        #     if User.user_level == 1:





#validations end here


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    # birthday = models.DateField()
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_level = models.CharField(max_length=2, default = 0)
    UserManager = UserManager()
    objects = models.Manager()
