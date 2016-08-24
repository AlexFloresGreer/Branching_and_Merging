from django.shortcuts import render, HttpResponse, redirect
from .models import Courses
from datetime import datetime

def index(req):
    context = {
        'courses': Courses.objects.all(),
        }
    return render(req, "courses/index.html", context)

def process(request):
    Courses.objects.create(name=request.POST['name'], description=request.POST['description'], created_at=datetime.now())
    return redirect('/courses')

def destroy(request, id):
    # Courses.objects.create(id=request.POST['id'])
    context ={
    'id' : Courses.objects.get(id = id),
    }
    return render(request, "courses/destroy.html", context)

def delete(request, id):
        Courses.objects.get(id=id).delete()
        return redirect('/courses')



# Entry.objects.filter(pub_date__year=2005).delete()
#https://docs.djangoproject.com/en/1.9/topics/db/queries/

#
# urlpatterns = [
#     url(r'^$', views.index),
#     url(r'^blogs$', views.blogs),
#     url(r'^comments/(?P<id>\d+)$', views.comments),
# ]
