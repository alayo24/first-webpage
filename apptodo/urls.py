"""TodoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from apptodo import views
from django.contrib.auth import views as auth_views




urlpatterns = [
     path('', views.home, name='home'),
     path('login', auth_views.login, {'template_name': 'apptodo/login.html'}),
     path('logout', auth_views.logout, {'template_name': 'apptodo/logout.html'}),
     path('portfolio', views.portfolio, name='portfolio'),
     path('new/todo', views.new_todo, name = 'new_todo'),
     path('mytodos', views.my_todos, name = 'mytodos'),
     path('edit/todo/<int:id>', views.edit_todo, name='edit_todo'),
     path('delete/todo/<int:id>', views.delete_todo, name= 'delete_todo'),




]
