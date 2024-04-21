from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import generics

from .models import Task
from .serializers import TaskSerializer


class TaskCreateViewSet(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        data['user'] = user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class TaskListViewSet(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user.pk)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response = Response(serializer.data)
        return response


class TaskEditViewSet(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def patch(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
