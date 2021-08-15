from django.db import models
# from student.models import Student, Choice
from django.forms.fields import CharField
from django.forms.widgets import NumberInput
from django.http import response

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=10,help_text="e.g Aisha")
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    genders=((u'M',u'Male'),
             (u'F',u'Female'),
             (u'O',u'Others'),)
    gender=models.CharField(max_length=1,choices=genders)
    nationalitys=((u'K',u'Kenya'),
                     (u'S',u'Sudan'),
                     (u'U',u'Uganda'),
                     (u'R',u'Rwanda'),)
    nationality=models.CharField(max_length=1,choices=nationalitys)
    county=models.CharField(max_length=12,default="Valid")
    # phone_number=models.PositiveIntegerField()
    email=models.EmailField()
    id_passport=models.CharField(max_length=12)
    parent_name=models.CharField(max_length=12)
    parent_contact=models.CharField(max_length=13)
    medical_report=models.FileField()
    registration_number=models.PositiveSmallIntegerField()
    room_number=models.CharField(max_length=8)
    big_sister=models.CharField(max_length=10,default="Valid")
    class_name=models.CharField(max_length=10)
    mentor_name=models.CharField(max_length=10)
    # device_number=models.ForeignKey('device_number',on_delete=models.CASCADE)
    # passport_photo=models.ImageField(upload_to="images")
    languages=((u'E',u'English'),
              (u'K',u'Kiswahili'),
              (u'A',u'Arabic'),
              (u'L',u'Local'), )
    language=models.CharField(max_length=3,choices=languages)
    laptop_number=models.CharField(max_length=3,null=True,blank=True)   #null used when we don't know the number/something

    def __str__(self):  #List first names only.
        return self.first_name