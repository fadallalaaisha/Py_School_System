
from django.db import models
from django.db.models.fields import CharField,DurationField
from django.db.models.enums import Choices
from django.forms.widgets import NumberInput
from django.http import response

# from django.http import request
# Create your models here.
class Trainer(models.Model):
    first_name=models.CharField(max_length=8)
    last_name=models.CharField(max_length=8)
    Choices=(
        ('M',"Male"),
        ('F',"Female"),
        ('O',"Other"),)
    gender=models.CharField(max_length=13,choices=Choices)
    Choices=((u'Kenya',u'Kenya'),
                (u'Uganda',u'Uganda'),
                (u'Sudan',u'Sudan'),)
    nationality=models.CharField(max_length=10,choices=Choices)
    email=models.EmailField()
    phone_number=models.CharField(max_length=13)
    bank_account=models.IntegerField()
    profession=models.CharField(max_length=30)
    salary=models.PositiveBigIntegerField()
    trainer_contract=models.FileField()
    id_number=models.IntegerField()
    course=models.CharField(max_length=12)
    cv=models.FileField(upload_to="documents/",blank=True,null=True)
    contract=models.FileField(upload_to="documents/",blank=True,null=True)
    profile_picture=models.ImageField(upload_to='images/',null=True,blank=True)
