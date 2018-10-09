from django.urls import path, include
from apptodo import views
from django.contrib.auth import views as auth_viewsp
path
from apptodo import views




urlpatterns = [
    path('index', views.index, name='index'),
    path('gallery', views.gallery, name='gallery'),
    path('aboutus', views.aboutus, name='aboutus')
    
    
    
    ]

    