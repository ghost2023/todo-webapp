from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from django.db.models import Q
from rest_framework.response import Response

from main.models import TaskModel
from .serializers import TaskSerializer


@api_view(["GET"])
def api_overview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail": "/task-detail/<slug:slug>/",
        "Create": "/task-create/",
        "Delete": "/task-delete/<slug:slug>/",
        "Update": "/task-update/<slug:slug>/",
    }
    return Response(api_urls)



@api_view(["GET"])
def task_list(request):
    q = request.GET.get("q") or ""
    task = TaskModel.objects.filter(Q(name__icontains=q) | Q(detail__icontains=q))

    if o := request.GET.get("o"):
        task = task.order_by(o)

    if l := request.GET.get("l"):
        if s := request.GET.get("s"):
            task = task[s : l + s]
        else:
            task = task[:l]

    else:
        if s := request.GET.get("s"):
            task = task[s : 20 + s]
        else:
            task = task[:20]

    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def task_detail(request, slug):
    task = TaskModel.objects.get(slug=slug)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def task_complete(request, slug):
    task = TaskModel.objects.get(slug=slug)
    task.completed = not task.completed
    task.save()

    return Response("Item changed Successfully")


@api_view(["POST"])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["POST"])
def task_update(request, slug):
    task = TaskModel.objects.get(slug=slug)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def task_delete(request, slug):
    task = TaskModel.objects.get(slug=slug)
    task.delete()

    return Response("Item Deleted Successfully")
