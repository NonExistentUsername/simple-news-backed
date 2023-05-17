from django.contrib.auth.models import User
from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "content",
            "created_by",
            "created_at",
            "updated_at",
            "is_published",
            "is_banned",
        )
        extra_kwargs = {
            "created_by": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "is_banned": {"read_only": True},
        }

    def save(self, **kwargs):
        self.validated_data["created_by"] = self.context["user"]
        return super().save(**kwargs)
