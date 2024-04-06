from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserCreateSerializer, UserListSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
