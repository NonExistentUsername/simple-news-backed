from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, mixins, status, views, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.serializers import UserRegisterSerializer, UserViewSerializer

from newsapp.utils import apply_custom_response


class UserRegisterView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    @apply_custom_response
    def create(self, request, *args, **kwargs):
        password = request.data.get("password")
        response = super().create(request, *args, **kwargs)

        user = User.objects.get(username=request.data.get("username"))
        user.set_password(password)
        user.save()

        return response


class GetMeView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
):
    serializer_class = UserViewSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
