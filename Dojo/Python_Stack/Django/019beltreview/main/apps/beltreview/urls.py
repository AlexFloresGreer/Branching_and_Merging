from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),  #this matches the "/" pathway
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books),
    url(r'^add$' ,views.add, name = 'add'),
    url(r'^showbookreview$', views.showbookreview),
    url(r'^showuser$', views.showuser),
]
