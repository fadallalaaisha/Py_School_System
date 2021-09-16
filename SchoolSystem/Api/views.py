# from django.shortcuts import render
from rest_framework import serializers, viewsets
from student.models import Student
from .serializers import ForAllSerializer
from trainer.models import Trainer
from course.models import Course

# Create your views here.Views recievces request from the http.
# Tells which metheds are we using to fiter data
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializers_class=ForAllSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()   
    serializer_class=ForAllSerializer 

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=ForAllSerializer    
