from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')       
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'adminapp/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    return render(request,'adminapp/index.html')