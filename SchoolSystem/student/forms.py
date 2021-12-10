from django import forms
from django.db.models.base import Model
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

# Meta tell the system how to work
        