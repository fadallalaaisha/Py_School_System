from django.urls import path
from django.urls.resolvers import URLPattern
from .views import register_Calendar

urlpatterns=[
    path("register/",register_Calendar, name='Calender'),
]