from django.shortcuts import render, HttpResponse, redirect
from django.conf.urls import url



def index(request):

    return render(request, "survey/index.html")

def process(request):
    print(request.method)
    if request.method == 'POST':
        request.session[ 'name' ] = request.POST[ 'name' ]
        request.session[ 'location' ] = request.POST[ 'location' ]
        request.session[ 'language' ] = request.POST[ 'language' ]
        request.session[ 'comment' ] = request.POST[ 'comment' ]
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    if 'count' not in request.session:
        request.session[ 'count' ] = 0
    request.session['count'] += 1
    return render(request, 'survey/result.html')


