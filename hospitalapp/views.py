from django.http import HttpResponse
from django.shortcuts import render
from . models import doctors,frontimage


# Create your views here.
# def home(request):
#     return HttpResponse("home")
def home(request):
    obj=doctors.objects.all()
    obj1=frontimage.objects.all()
    return render(request,'index.html',{'result':obj,'fimage':obj1})


























