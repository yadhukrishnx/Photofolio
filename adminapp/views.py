from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from . models import UserDetails, ProfessionalExperience, Education
from . forms import UserDetailsForm, ProfessionalExperienceForm, EducationForm
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

def editprofile(request):
    user_details = UserDetails.objects.first()
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, request.FILES,instance=user_details)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('home')
    else:
        form = UserDetailsForm()
    return render(request, 'adminapp/editprofile.html', {'form': form})
def editphotofolio(request):
    experiences = ProfessionalExperience.objects.all()
    education = Education.objects.all()
    if request.method == 'POST':
        form1 = ProfessionalExperienceForm(request.POST)
        form2 = EducationForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, 'Experience added successfully')
            return redirect('home')
        elif form2.is_valid():  
            form2.save()
            messages.success(request, 'Education added successfully')
            return redirect('home')
    else:
        form1 = ProfessionalExperienceForm()
        form2 = EducationForm()
    return render(request, 'adminapp/editphotofolio.html', {'form1': form1, 'experiences': experiences, 'form2': form2, 'education': education})
