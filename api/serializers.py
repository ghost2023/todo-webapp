from django.db.models import fields
from rest_framework import serializers
from main import models
from main.models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"
