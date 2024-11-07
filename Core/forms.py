from django import forms
from .models import Task

class TareaForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
