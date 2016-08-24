from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    countries = models.Countries.objects.filter(languagetocountry__language='slovene')
    languages = models.Languages.objects.filter(language='slovene').order_by('-percentage')

    # cities = models.Countries.objects.filter(languagetocountry__language='slovene')
    # languages = models.Languages.objects.filter(language='slovene')

    # prints the queries
    print (50*"*")
    print countries.query
    print (50*"*")
    print languages.query
    print (50*"*")
    return render(req, 'worldApp/index.html', context={'countries':countries, 'languages': languages})