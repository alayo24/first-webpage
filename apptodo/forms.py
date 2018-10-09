from django import forms
from .models import TodoApp



class TodoAppForm(forms.ModelForm):
    class Meta:
        model =TodoApp
        fields = ('name', 'content', 'description', 'time_added', 'due_date', 'created')
        #fields= '__all__'



