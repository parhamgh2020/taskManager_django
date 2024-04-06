from rest_framework.viewsets import generics

from .models import Task
from .serializers import TaskSerializer


class TaskCreateViewSet(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListViewSet(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
