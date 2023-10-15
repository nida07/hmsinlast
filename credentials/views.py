from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# message import
from django.contrib import messages,auth

from . models import biometric
from .forms import BiometricForm

# Create your views here.
# login page data readings
def login(request):
    if request.method=='POST':

        username=request.POST['uname']
        password=request.POST['password']
        # the verification of user name and password inthe form of dbcolname=function variable name
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            return render(request,'viewuser.html')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')


# registration page data reading
def register(request):
    if request.method=='POST':
        username=request.POST['uname']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        # email,username exist ,password confirmation
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save();
            #     if registration success redirect to login page
            return redirect('login')

            # print("User Created")
        else:
            messages.info(request,"Password not Match")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')



# logout details
def logout(request):
    auth.logout(request)

    # back to home page
    return redirect('/')
#if he logout he will redirst to home page

def viewuser(request):
    return render(request,'viewuser.html')


# user biometric updation
def user_biometric_edit(request):
    if request.method=='POST':
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        bloodpressure=request.POST.get('bloodpressure')
        bloodgroup=request.POST.get('bloodgroup')
        bio_obj=biometric(weight=weight,height=height,bloodpressure=bloodpressure,bloodgroup=bloodgroup)
        bio_obj.save()

        return redirect('viewuser')
    else:
        return render(request,'user_biometric_edit.html')
def update_bio(request,id):
    bios=biometric.objects.get(id=id)
    bioform=BiometricForm(request.POST or None,request.FILES,instance=bios)
    if bioform.is_valid():
        bioform.save()
        return redirect('viewuser')
    return render(request,'user_biometric_edit.html',{'bioform':bioform,'bios':bios})

def user_login(request):
    return render(request,"user_login.html")

def user_register(request):
    return render(request,"user_register.html")

# def base(request):
#     return render(request,"base.html")