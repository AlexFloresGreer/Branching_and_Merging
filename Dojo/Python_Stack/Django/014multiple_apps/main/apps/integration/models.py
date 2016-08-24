from __future__ import unicode_literals
from django.db import models
from ..registration.models import User
from ..courses.models import Courses
# Create your models here.


class Add_User(models.Model):
    user = models.ForeignKey(User)
    courses = models.ForeignKey(Courses)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
