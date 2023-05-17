from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_by", "updated_at", "created_at", "is_published", "is_banned")
    list_filter = ("created_by", "is_published", "is_banned")
    search_fields = ("title", "content")
    ordering = ("-created_at",)


admin.site.register(News, NewsAdmin)

# Register your models here.
