import django_mongodb_backend
from django.db import models


class Task(models.Model):
    _id = django_mongodb_backend.fields.ObjectIdAutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)  # type: ignore
    userId = django_mongodb_backend.fields.ObjectIdField()
