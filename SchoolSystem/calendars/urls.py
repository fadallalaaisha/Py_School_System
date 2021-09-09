# from django.shortcuts import render
# from django import urls# 
# from .views import register_Calendar
# path('admin/', admin.site.urls),
    # path("register/",register_Calendar, name='Calender'),
    # path("list/",calendar_list,name="calendar_list"),


from django.urls.resolvers import URLPattern
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns=[
    
    path('<int:year>/<str:month>',views.register_calendar,
    name='register_calendar'),
]

