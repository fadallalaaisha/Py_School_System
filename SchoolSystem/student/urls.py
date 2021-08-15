from django import urls
from django.urls.resolvers import URLPattern

from django.urls import path
from .views import register_student, student_list

urlpatterns=[
    path("register/",register_student, name='student'),
    path("list/",student_list,name="student_list"),
    # path("list/",student_list,name="student_list"),
]
# if settings.DEBUG:
#     urlpatters = static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)