from django.http import JsonResponse
from .models import Task
from bson import ObjectId
import json


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
    request_METHOD = request.method
    if request_METHOD == "GET":
        tasks = list(Task.objects.all().values())  # type: ignore
        tasks = convert_objectid(tasks)
        return JsonResponse({"success": True, "response": tasks})


def getTask(request, pk):
    _ = request
    task = Task.objects.get(_id=pk)  # type: ignore
    task = convert_objectid(task)
    return JsonResponse({"success": True, "response": task})


def createTask(request):
    request_METHOD = request.method
    if request_METHOD == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            description = data.get("description")
            done = data.get("done", False)
            userId = data.get("userId")

            if not title or not userId:
                return JsonResponse(
                    {"success": False, "error": "Title and userId are required"},
                    status=400,
                )

            task = Task.objects.create(  # type: ignore
                title=title,
                description=description,
                done=done,
                userId=userId,
            )

            task_dict = convert_objectid(task)
            return JsonResponse({"success": True, "response": task_dict})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)


def updateTask(request, pk):
    request_METHOD = request.method
    if request_METHOD == "PUT":
        try:
            data = json.loads(request.body)
            title = data.get("title")
            description = data.get("description")
            done = data.get("done", False)
            userId = data.get("userId")

            task = Task.objects.get(_id=pk)  # type: ignore
            task.title = title
            task.description = description
            task.done = done
            task.userId = userId
            task.save()  # type: ignore

            task_dict = convert_objectid(task)
            return JsonResponse({"success": True, "response": task_dict})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)


def deleteTask(request, pk):
    request_METHOD = request.method
    if request_METHOD == "DELETE":
        try:
            task = Task.objects.get(_id=pk)  # type: ignore
            task.delete()  # type: ignore
            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)
