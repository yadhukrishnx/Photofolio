from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from adminapp.models import UserDetails,ProfessionalExperience, Education,Projects,Services
from django.core.mail import send_mail

from django.conf import settings
from django.contrib import messages

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
    if request.method == 'POST':
       
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

       

        full_message = f"{message}\n\nMail sent by {name} ({email})"
        try:
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully')
            return redirect(reverse_lazy('contact'))
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
    userdetail = UserDetails.objects.first()
    return render(request, 'viewerapp/contact.html', {'userdetail': userdetail})

def gallery_single(request, id):    
    project = get_object_or_404(Projects, id=id)
    return render(request, 'viewerapp/gallery-single.html',{'project': project})