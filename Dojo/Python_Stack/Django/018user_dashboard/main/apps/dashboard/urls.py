from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^registerprocess$', views.registerprocess),
    url(r'^signin$', views.signin),
    url(r'^signinprocess$', views.signinprocess),
    url(r'^dashboard$', views.dashboardadmin),
    url(r'^addnewuser$', views.addnewuser),
    url(r'^addnewuserprocess$', views.addnewuserprocess),
    url(r'^logout$', views.logout),
]
