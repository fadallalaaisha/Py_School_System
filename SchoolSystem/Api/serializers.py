from django.db import models
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course


class ForAllSerializer(serializers.ModelSerializer):
    # class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=("first_name","last_name","age",)

        model=Trainer
        fields=("first_name","last_name","age",)

        model=Course
        fields=("course_code","course_duration","course_name")



# class TrainerSerializer(serializers.ModelSerializer)
#       class Meta:        