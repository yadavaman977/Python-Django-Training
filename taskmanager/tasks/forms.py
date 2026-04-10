from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter task title...',
                'class': 'form-input',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Optional description...',
                'rows': 4,
                'class': 'form-input',
            }),
        }