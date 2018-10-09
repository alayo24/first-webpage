from time import strftime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date
from timezone_field import TimeZoneFormField



# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=())
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    Location = models.CharField(max_length=100, default='my Location default')




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)




class TodoApp(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField(blank=False, default='')
    description = models.TextField(blank=False)
    time_added = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateTimeField()
    created =models.DateTimeField()

    class Meta:
       ordering = ["-time_added"]

    def __str__(self):
        return self.title

#to let django know u created a model/table go to ur terminal and type (python manage.py makemigrations)
#then write python manage.py migrate
#to create admin python manage.py createsuperuser
