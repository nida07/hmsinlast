from django.db import models

# Create your models here.
class biometric(models.Model):
    height=models.IntegerField()
    weight=models.IntegerField()
    bloodpressure=models.CharField(max_length=100)
    bloodgroup=models.CharField(max_length=15)
