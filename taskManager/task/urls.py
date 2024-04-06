from django.urls import path

from .views import TaskListViewSet, TaskCreateViewSet

urlpatterns = [
    path('create', TaskCreateViewSet.as_view()),
    path('list', TaskListViewSet.as_view()),
]
