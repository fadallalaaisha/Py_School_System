from django import forms
from django.db.models.base import Model
#handles data
from .models import Student
# from django.db.models.base import Model

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

# Meta tell the system how to work
        