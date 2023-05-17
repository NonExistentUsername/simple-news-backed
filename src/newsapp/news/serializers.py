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
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["created_by"] = self.instance.created_by
        return super().update(instance, validated_data)
