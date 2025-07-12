from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.createTask),
    path("task/", views.getTasks),
    path("task/<str:pk>/", views.getTask),
    path("task/<str:pk>/", views.updateTask),
    path("task/<str:pk>/", views.deleteTask),
]
