import typing as t

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from news.views import NewsView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"news", NewsView)

urlpatterns: t.List[t.Any] = [] + router.urls
