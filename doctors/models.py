#
#
# # Create your models here.
from django.db import models
#
# # Create your models here.
class dregister(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    doj=models.DateField(auto_now_add=True)
    exp=models.IntegerField()
    dept=models.CharField(max_length=30)
    uname=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


#
#
