from django import forms
from django.db.models.base import Model
from .models import Trainer
# from django.forms import fields

class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Trainer
        fields="__all__"

