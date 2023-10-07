from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def home(request):
#     return HttpResponse("home")
def home(request):
    return render(request,'index.html')
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     values=x+y
#     values2=x-y
#     values3=x/y
#     values4=x*y
#
#
#     return render(request,'result.html',{'res':values,'res2':values2,'res3':values3,'res4':values4})
#
# def contact(request):
#     #value calling check the page of contact.html {{no}} avinde nokk ullile value ne kaanikkum no oru dict le key aaan
#     name="call you nida"
#     return render(request,"contact.html",{'no':name})
# def details(request):
#     return render(request,'details.html')
# def thanks(request):
#     return render(request,'thanks.html')
# def about(request):
#     return render(request,'about.html')
