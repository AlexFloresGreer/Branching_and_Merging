from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.none),
    url(r'^ninjas/$', views.index),
    url(r'^ninjas/(?P<id>\w+)$', views.ninjas),


]
