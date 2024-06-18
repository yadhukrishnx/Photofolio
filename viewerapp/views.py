from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'viewerapp/index.html')
def about(request):
    return render(request, 'viewerapp/about.html')

def gallery(request):
    return render(request, 'viewerapp/gallery.html')

def services(request):
    return render(request, 'viewerapp/services.html')

def contact(request):
    return render(request, 'viewerapp/contact.html')