from __future__ import unicode_literals
from django.db import models



class Courses(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
