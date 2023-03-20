from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, mixins, status, views, viewsets
from rest_framework.response import Response
from users.serializers import UserSerializer


class UserView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
