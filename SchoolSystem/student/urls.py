from django.urls import path
from .views import delete_student, edit_student, register_student,student_list, student_profile

urlpatterns=[
    path("register/",register_student, name='student'),
    path("list/", student_list,name="student_list"),
    path("edit/<int:id>/",edit_student, name="edit_student"),
    path("profile/<int:id>/",student_profile, name="student_profile"),
    path("delete/<int:id>/",delete_student,name="delete_student")
    ]




