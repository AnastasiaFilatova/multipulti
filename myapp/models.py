from django.db import models
from enum import Enum




Market = (('TR','TR'),
          ('EN', 'EN'),
          ('SE', 'SE'))

class Size(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    market = models.CharField(max_length=10)




class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sizes = models.ManyToManyField(Size)
    


