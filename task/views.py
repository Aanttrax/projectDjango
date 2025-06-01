from django.http import JsonResponse
from .models import Task
from bson import ObjectId


def convert_objectid(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, dict):
        return {k: convert_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_objectid(i) for i in obj]
    else:
        return obj


def getTasks(request):
    _ = request
    tasks = list(Task.objects.all().values())  # type: ignore
    tasks = convert_objectid(tasks)
    return JsonResponse({"success": True, "response": tasks})
