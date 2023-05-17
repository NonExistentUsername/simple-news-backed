import typing as t

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from users.views import GetMeView, UserRegisterView

router = routers.DefaultRouter()
router.register(r"register", UserRegisterView)

urlpatterns: t.List[t.Any] = [
    path(
        "login/",
        views.obtain_auth_token,
    ),
] + router.urls

users_urlpatterns = [
    path(
        "me/",
        GetMeView.as_view(
            {
                "get": "retrieve",
            }
        ),
    ),
]
