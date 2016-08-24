from django.shortcuts import render, HttpResponse, redirect
from .models import Emails
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):
    return render(request, 'emailvalidation/index.html')

def process(request):
    printemail = request.POST['email']
    if EMAIL_REGEX.match(printemail):
        Emails.objects.create(email=printemail,created_at=datetime.now())
        context ={
            'printemail' : printemail,
            'allemails': Emails.objects.all(),
        }
        return render(request, 'emailvalidation/success.html', context)
    elif not EMAIL_REGEX.match(printemail):
        data = {'novalidemail' : "novalidemail"}
        return render(request, 'emailvalidation/index.html', data)


def success(request):
    return render(request, 'emailvalidation/success.html')
