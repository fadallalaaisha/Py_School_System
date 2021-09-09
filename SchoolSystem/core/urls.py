# from typing import Pattern
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from django import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from.views import home

urlpatterns=[
    path('',home, name="home_page"),
    path('course/', Course, name='Course'),
    path('trainer/',Trainer, name='Trainer'),
    path('student/', Student, name='Student'),
]

# from django.urls import path
# from .views import register_trainer, trainer_list

# urlpatterns=[
#     path("register/",register_trainer, name="trainer"),
#     path("list/", trainer_list,name="trainer_list")
# ]


