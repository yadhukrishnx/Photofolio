from django.shortcuts import get_object_or_404, render
from adminapp.models import UserDetails,ProfessionalExperience, Education,Projects,Services

def index(request):
    return render(request, 'viewerapp/index.html')
def about(request):
    user_details = UserDetails.objects.first()
    experiences = ProfessionalExperience.objects.all()
    educations = Education.objects.all()
    return render(request, 'viewerapp/about.html', {'user_details': user_details,'experiences': experiences,'educations': educations})

def gallery(request):
    projects=Projects.objects.all()
    return render(request, 'viewerapp/gallery.html',{'projects': projects})

def services(request):
    services=Services.objects.all()
    return render(request, 'viewerapp/services.html',{'services': services})

def contact(request):
    userdetail = UserDetails.objects.first()
    return render(request, 'viewerapp/contact.html',{'userdetail': userdetail})

def gallery_single(request, id):    
    project = get_object_or_404(Projects, id=id)
    return render(request, 'viewerapp/gallery-single.html',{'project': project})