from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from news.urls import urlpatterns as news_urlpatterns
from users.urls import urlpatterns as auth_urlpatterns
from users.urls import users_urlpatterns

urlpatterns = [
    path("api/news/", include(news_urlpatterns)),
    path("api/auth/", include(auth_urlpatterns)),
    path("api/users/", include(users_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns.append(path("api-auth/", include("rest_framework.urls")))
    urlpatterns.append(path("admin/", admin.site.urls))
    urlpatterns.append(*static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
