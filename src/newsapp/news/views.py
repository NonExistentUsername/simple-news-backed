from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from news.models import News
from news.serializers import NewsSerializer
from rest_framework import mixins, status, views, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class NewsView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
):
    serializer_class = NewsSerializer
    queryset = News.objects.filter(
        is_published=True,
        is_banned=False,
    )

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["created_by", "is_published", "title", "is_banned"]

    def get_queryset(self):
        result = super().get_queryset()

        if self.request.user.is_staff:
            result = News.objects.all()

        if not self.request.user.is_anonymous:
            result = News.objects.filter((Q(is_published=True) & Q(is_banned=False)) | Q(created_by=self.request.user))

        content = self.request.query_params.get("content")
        if content:
            result = result.filter(content__icontains=content)

        return result

    def update(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return super().update(request, *args, **kwargs)

        object: News = self.get_object()
        if self.request.user != object.created_by:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if object.is_banned:
            return Response(status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
