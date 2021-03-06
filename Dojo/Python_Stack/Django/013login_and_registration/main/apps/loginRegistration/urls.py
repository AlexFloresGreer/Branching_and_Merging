from django.conf.urls import url
from . import views                   #add this line

urlpatterns = [
  url(r'^$', views.index),  #this matches the "/" pathway
  url(r'^register$', views.register),
  url(r'^login$', views.login),
  url(r'^success/(?P<name>\w+)$', views.success)
]
