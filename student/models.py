# from _typeshed import self
from django.db import models
from django.forms.fields import CharField
from django.forms.widgets import NumberInput
from django.http import response
import datetime

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
    nationalitys=((u'Kenya',u'Kenya'),
                     (u'Sudan',u'Sudan'),
                     (u'Uganda',u'Uganda'),
                     (u'Rwanda',u'Rwanda'),)
    nationality=models.CharField(max_length=10,choices=nationalitys)
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
    passport_photo=models.ImageField(upload_to='images',null=True, blank=True)
    languages=((u'English',u'English'),
              (u'Kiswahili',u'Kiswahili'),
              (u'Arabic',u'Arabic'),
              (u'Others',u'Others'), )
    language=models.CharField(max_length=10,choices=languages)
    admintion_number=models.CharField(max_length=13)
    student_number=models.CharField(max_length=13,null=True,blank=True)
    laptop_number=models.CharField(max_length=3,null=True,blank=True)   #null used when we don't know the number/something

    def __str__(self):  #List first names only.
        return self.first_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

def test_full_name_contains_first_name(self):
    self.assertin(self.student.first_name,self.student.full_name())

def test_full_name_contain_last_name(self):
    self.assertin(self.student.last_name,self.student.full_name()) 


    def test_year_of_birth(self):
        year=datetime.dateTime.now(). year - Student.age
        self.assertEqual(year, self.student.year_of_birth()) 

    def test_student_regristrarrion_view(student):
        self.data= {"first_name": self.Student.first_name, "last_name":self.Student.last_name,
        "age":self.Student.age}

        url=reversed("register_student")
        response= self.Client.post(url, self.data)
        self.assertEqual(response.startus_code, 200)    



        
