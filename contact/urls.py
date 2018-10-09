from django.urls import path, include
from contact import views




urlpatterns = [
    path('contact.html', views.contact, name='contact'),


    ]