from django.db import models

class CitizenDate(models.Model):
    type_hash = models.CharField(max_length=200)
    date = models.DateTimeField('date published', auto_now=True)
    owner = models.CharField(max_length=200)
