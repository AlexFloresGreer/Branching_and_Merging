from django.conf.urls import url
from views import new, edit, destroy, create, update, users_w_id, users


# Remember, the 'products' portion of the url was devoured by the main urls.py file
urlpatterns = [
    # This route deals w/ GET and POST to users (either index or create)
    url(r'^$', users),
    # url(r'^$', index),
    # url(r'^create$', create),
    url(r'^new$', new),
    # # This route deals w/ GET and POST to /users/<id> (either update or show)
    url(r'^(?P<id>\d+)/$', users_w_id),
    url(r'^(?P<id>\d+)/$', update),
    url(r'^(?P<id>\d+)/edit/$', edit),
    url(r'^(?P<id>\d+)/destroy/$', destroy),
]
