from django.http import HttpResponse


def index(request):
    _ = request
    return HttpResponse(b"<h1>Hello, world.You nou're at the task index.</h1>")
