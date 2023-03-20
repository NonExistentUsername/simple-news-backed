from django.shortcuts import render
from news.models import News
from news.serializers import NewsSerializer
from rest_framework import mixins, views, viewsets


class NewsView(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
