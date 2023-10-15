from django.db import models

# Create your models here
# customize the images in the home page section to the client using this
class doctors(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
        #this function will used to show names in admin panel
class frontimage(models.Model):
    images=models.ImageField(upload_to='fimage')
    names=models.CharField(max_length=250)
    names2=models.CharField(max_length=250)
    descs=models.TextField()
    def __str__(self):
        return self.names




