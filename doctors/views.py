

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# message import
from django.contrib import messages,auth
from .models import dregister

def d_login(request):
    return render(request,'d_login.html')
def d_register(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        exp=request.POST.get('exp')
        doj=request.POST.get('doj')
        dept=request.POST.get('dept')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        # email,username exist ,password confirmation
        if password==cpassword:
            if dregister.objects.filter(uname=uname).exists():
                messages.info(request,"Username is already Taken")
                return redirect('d_register')
            elif dregister.objects.filter(email=email).exists():
                messages.info(request,"Email is already Taken")
                return redirect('d_register')
            else:
                dreg=dregister(uname=uname,fname=fname,lname=lname,email=email,password=password,doj=doj,exp=exp,dept=dept)
                dreg.save();
            #     if registration success redirect to login page
            return render(request,'d_login.html')

            # print("User Created")
        else:
            messages.info(request,"Password not Match")
            return redirect('d_register')
        return redirect('/')
    return render(request,'d_register.html')
