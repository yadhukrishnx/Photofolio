from django.shortcuts import render
from adminapp.models import UserDetails,ProfessionalExperience, Education
# Create your views here.

def index(request):
    return render(request, 'viewerapp/index.html')
def about(request):
    user_details = UserDetails.objects.first()
    experiences = ProfessionalExperience.objects.all()
    educations = Education.objects.all()
    return render(request, 'viewerapp/about.html', {'user_details': user_details,'experiences': experiences,'educations': educations})

def gallery(request):
    return render(request, 'viewerapp/gallery.html')

def services(request):
    return render(request, 'viewerapp/services.html')

def contact(request):
    return render(request, 'viewerapp/contact.html')