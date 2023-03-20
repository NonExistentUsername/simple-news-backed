from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, mixins, status, views, viewsets
from rest_framework.response import Response
from users.serializers import UserSerializer


class UserView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return super().update(request, *args, **kwargs)

        if self.request.user.is_anonymous:
            return Response(status=status.HTTP_404_NOT_FOUND)

        object: User = self.get_object()

        if object != self.request.user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return super().update(request, *args, **kwargs)
