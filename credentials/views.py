from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# message import
from django.contrib import messages,auth

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
            return redirect('/')
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
    return redirect('/')