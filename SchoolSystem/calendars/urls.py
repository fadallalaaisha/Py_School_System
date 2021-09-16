from calendars.utils import Calendar
from django.urls.conf import path
from . import views
# from SchoolSystem import calendars

urlpatterns=[
      path("register/",views.CalendarView.as_view, name='Calender'),
      path("list/",Calendar,name="calendar_list"),

]
from django.conf.urls import url

# app_name = 'cal'
# urlpatterns = [
#     url(r'^index/$', views.index, name='index'),
#     url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # here
# ]












# from django.urls.resolvers import URLPattern
# from django.contrib import admin
# from django.urls import path
# from .import views
# urlpatterns=[
    
#     path('<int:year>/<str:month>',views.register_calendar,
#     name='register_calendar'),
# ]

