from django.db import models

# Create your models here
# customize the images in the home page section to the client using this
class doctors(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
