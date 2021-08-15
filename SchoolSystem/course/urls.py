

from django.urls import path
from .views import register_Course

urlpatterns=[
    path("register/", register_Course, name="Course"),
]

