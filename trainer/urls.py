
# from django.urls.resolvers import URLPattern
# from django import urls
from django.urls import path
from .views import delete_trainer, edit_trainer, register_trainer, trainer_list, trainer_profile


urlpatterns=[
    path("register/",register_trainer, name="Trainer"),
    path("list/",trainer_list,name="trainer_list"),
    path("edit/<int:id>/",edit_trainer, name="edit_trainer"),
    path("profile/<int:id>/",trainer_profile, name="trainer_profile"),
    path("delete/<int:id>/",delete_trainer,name="delete_trainer"),
]








