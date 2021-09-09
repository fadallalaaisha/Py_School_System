# from django.urls.resolvers import URLPattern
# from django import urls
from django.urls import path
from .views import delete_course, edit_course, register_Course, course_list

urlpatterns=[
    path("register/", register_Course, name="Course"),
    path("list/",course_list,name="course_list"),
    path("edit/<int:id>/",edit_course, name="edit_course"),
    # path("delete/<int:id>/",edit_course, name="edit_course"),
    path("delete/<int:id>/",delete_course,name="delete_course")


]
