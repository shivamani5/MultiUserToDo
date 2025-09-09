from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date"}), required=False
    )
    class Meta:
        model=Task
        fields=['title','description','is_completed','priority','due_date']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "priority": forms.Select(attrs={"class": "form-select"}),
            "due_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "is_completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

