from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from news.urls import urlpatterns as news_urlpatterns
from rest_framework.authtoken import views
from users.urls import urlpatterns as users_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/news/", include(news_urlpatterns)),
    path("api/auth/login/", views.obtain_auth_token),
    path("api/auth/", include(users_urlpatterns)),
]

if settings.DEBUG:
    urlpatterns.append(*static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
