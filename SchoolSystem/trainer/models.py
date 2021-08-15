from django.db import models
from django.db.models.fields import CharField,DurationField
from django.db.models.enums import Choices

from django.http import request

# Create your models here.


class Trainer(models.Model):
    first_name=models.CharField(max_length=8)
    last_name=models.CharField(max_length=8)
    genders=((u'M',u'Male'),
                    (u'F',u'Female'),
                    (u'O',u'Others'),
    )
    gender=models.CharField(max_length=1,choices=genders)
    place=((u'K',u'Kenya'),
                (u'U',u'Uganda'),
                (u'S',u'Sudan'),
    )
    nationality=models.CharField(max_length=1,choices=place)
    profile_picture=models.ImageField()
    email=models.EmailField()
    bank_account=models.IntegerField()
    trainer_contract=models.FileField()
    profession=models.CharField(max_length=30)
    salary=models.PositiveBigIntegerField()
    trainer_CV=models.FileField()
    id_number=models.IntegerField()
    # experience=models.PositiveSmallIntegerField()
    # phone_number=models.CharField()
    contract=models.FileField()

    
