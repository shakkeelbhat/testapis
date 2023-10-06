from django.db import models

# Create your models here.
class BoxModel(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    shape = models.CharField(max_length=50,null=False,blank=False)
    price = models.IntegerField()

