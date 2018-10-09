from django.db import models
from django.utils import timezone

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    comment = models.TextField(max_length=200, blank=False)
    time_added = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
       ordering = ["-time_added"]

    def __str__(self):
        return self.title
