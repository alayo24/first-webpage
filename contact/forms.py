from django import forms
from .models import contact


class contactForm(forms.ModelForm):
        class Meta:
            model = contact
            fields = ('name', 'email', 'comment', 'time_added')