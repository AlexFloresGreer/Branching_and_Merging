from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect, HttpResponse
from .models import User
from django.contrib import messages
from datetime import datetime
import bcrypt



def index(request):
	return render(request,'dashboard/index.html')

def register(request):
    return render(request, 'dashboard/register.html')

def registerprocess(request):
	errors = False
	check1 = User.UserManager.first_name(request.POST['first_name'])
	check1_char = User.UserManager.first_name_charcheck(request.POST['first_name'])
	check2 = User.UserManager.last_name(request.POST['last_name'])
	check3 = User.UserManager.reg_email(request.POST['email'])
	check4 = User.UserManager.password(request.POST['password'])
    # check5 = User.UserManager.password(request.POST['password'])
	# check6 = Userlog.UserManager.birthday(request.POST['birthday'])
	print request.POST['password']
	print bcrypt.gensalt()
	check5 = User.UserManager.confirm_password(request.POST['password'] ,request.POST['confirm_password'])
	if check1[0] == False:
		messages.add_message(request, messages.INFO, "Invalid firstname", extra_tags="regtag")
		errors = True
	if check1_char[0] == False:
		messages.add_message(request, messages.INFO, "Invalid characters in firstname", extra_tags="regtag")
		errors = True
	if check2[0] == False:
		messages.add_message(request, messages.INFO, "Invalid lastname", extra_tags="regtag")
		errors = True
	if check3[0] == False:
		messages.add_message(request, messages.INFO, "Invalid Email", extra_tags="regtag")
		errors = True
	if check4[0] == False:
		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
		print check4[1]
		errors = True
	if check5[0] == False:
		messages.add_message(request, messages.INFO, "Passwords don't match", extra_tags="regtag")
		errors = True
	# if check6[0] == False:
	# 	print check6[1]
	# 	messages.add_message(request, messages.INFO, "Invalid BirthDate", extra_tags="regtag")
	# 	errors = True
	# To check DB whether Email already registered or not....
	if User.objects.filter(email = request.POST['email']):
	    messages.add_message(request, messages.INFO, "This email already existed!", extra_tags="regtag")
	    errors = True
	# Errors Route
	if errors == True:
		return redirect('/register')
	elif (check1[0] == True & check2[0] == True & check3[0] == True & check4[0] == True & check5[0] == True  ):
		user = User.UserManager.create(first_name=check1[1], last_name=check2[1], email=check3[1], password=check4[1])
		request.session['user'] = check1[1]
        if user.id == 1:
            print user.id
            print "user" *10
            print user.user_level
            user.user_level = 9
            user.save()
            print user.user_level
	    # messages.add_message(request, messages.INFO, "Successfully Registered", extra_tags="regtag")
            return redirect('/dashboard')

def signin(request):
	return render(request,'dashboard/signin.html')
#login process
def signinprocess(request):
	check7 = User.UserManager.log(request.POST['email'], request.POST['password'])
	if check7[0] == False:
		messages.add_message(request, messages.INFO, check7[1], extra_tags='logtag')
		print check7[1]
		return redirect('/signin')
	else:
		request.session['user'] = check7[1]
		messages.add_message(request, messages.INFO, "Successfully logged in!", extra_tags="regtag")
		return redirect('/dashboard')

def dashboardadmin(request):
    context={
        'users': User.objects.all(),
    }
    return render(request,'dashboard/dashboardadmin.html', context)

def addnewuser(request):
    return render(request,'dashboard/addnewuser.html')

def addnewuserprocess(request):
    	errors = False
    	check1 = User.UserManager.first_name(request.POST['first_name'])
    	check1_char = User.UserManager.first_name_charcheck(request.POST['first_name'])
    	check2 = User.UserManager.last_name(request.POST['last_name'])
    	check3 = User.UserManager.reg_email(request.POST['email'])
    	check4 = User.UserManager.password(request.POST['password'])
        # check5 = User.UserManager.password(request.POST['password'])
    	# check6 = Userlog.UserManager.birthday(request.POST['birthday'])
    	print request.POST['password']
    	print bcrypt.gensalt()
    	check5 = User.UserManager.confirm_password(request.POST['password'] ,request.POST['confirm_password'])
    	if check1[0] == False:
    		messages.add_message(request, messages.INFO, "Invalid firstname", extra_tags="regtag")
    		errors = True
    	if check1_char[0] == False:
    		messages.add_message(request, messages.INFO, "Invalid characters in firstname", extra_tags="regtag")
    		errors = True
    	if check2[0] == False:
    		messages.add_message(request, messages.INFO, "Invalid lastname", extra_tags="regtag")
    		errors = True
    	if check3[0] == False:
    		messages.add_message(request, messages.INFO, "Invalid Email", extra_tags="regtag")
    		errors = True
    	if check4[0] == False:
    		messages.add_message(request, messages.INFO, "Invalid password", extra_tags="regtag")
    		print check4[1]
    		errors = True
    	if check5[0] == False:
    		messages.add_message(request, messages.INFO, "Passwords don't match", extra_tags="regtag")
    		errors = True
    	# if check6[0] == False:
    	# 	print check6[1]
    	# 	messages.add_message(request, messages.INFO, "Invalid BirthDate", extra_tags="regtag")
    	# 	errors = True
    	# To check DB whether Email already registered or not....
    	if User.objects.filter(email = request.POST['email']):
    	    messages.add_message(request, messages.INFO, "This email already existed!", extra_tags="regtag")
    	    errors = True
    	# Errors Route
    	if errors == True:
                # print "error" * 20
    		return redirect('/addnewuser')
    	elif check1[0] == True & check2[0] == True & check3[0] == True & check4[0] == True & check5[0] == True :
    	    user = User.UserManager.create(first_name=check1[1], last_name=check2[1], email=check3[1], password=check4[1])
            print "elif" * 20
            request.session['user'] = check1[1]
            print "*" * 20
            if user.id == 1:
                print user.id
                print "second" *10
                print user.user_level
                user.user_level = 9
                user.save()
                print user.user_level
    		# messages.add_message(request, messages.INFO, "Successfully Registered", extra_tags="regtag")
    	        return redirect('/dashboard')




def logout(request):
	del request.session['user']
	return redirect('/')
