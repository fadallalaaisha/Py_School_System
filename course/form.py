from django import forms
from django.db.models.base import Model
from .models import Course
#handles data
# from django.forms import fields

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"