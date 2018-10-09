from django.shortcuts import render
from apptodo import views


# Create your views here.

def index(request):
    return render(request, 'play/index.html')


def gallery(request):
    return render(request, 'play/gallery.html')




def aboutus(request):
    return render(request, 'play/aboutus.html')