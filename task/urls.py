from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.getTasks),
]
