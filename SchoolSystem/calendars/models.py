from django.db import models

# Create your models here.

from django.http import response
from django.forms.fields import CharField
from django.forms.widgets import NumberInput

class Calendar(models.Model):
    event_name=models.CharField(max_length=10)
    event_month=models.CharField(max_length=10)
    event_date=models.DateTimeField()
    event_organizer=models.CharField(max_length=10)
    event_duration=models.TimeField()
    event_golds=models.CharField(max_length=14)
    event_appoved=models.CharField(max_length=12)
    event_attented_by=models.CharField(max_length=3)
