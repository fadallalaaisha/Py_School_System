from django.db import models
# Create your models here.
from django.forms.fields import CharField
from django.forms.widgets import NumberInput
from django.http import response

class Course(models.Model):
    course=models.CharField(max_length=14)
    course_code=models.IntegerField()
    syllabus=models.FileField()
    course_duration=models.DateField()
    trainer_course=models.CharField(max_length=10)
    project=models.TextField()

