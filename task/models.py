from django_mongodb_backend.fields import ObjectIdAutoField, ObjectIdField
from django.db import models


class Task(models.Model):
    _id = ObjectIdAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)  # type: ignore
    userId = ObjectIdField()

    class Meta:
        db_table = "tasks"
