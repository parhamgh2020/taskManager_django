from django.urls import path

from .views import TaskListViewSet, TaskCreateViewSet, TaskEditViewSet

urlpatterns = [
    path('create/', TaskCreateViewSet.as_view()),
    path('update/<int:pk>', TaskEditViewSet.as_view(), name='task-edit'),
    path('list/', TaskListViewSet.as_view()),
]
