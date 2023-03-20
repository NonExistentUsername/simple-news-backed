from django.contrib.auth.models import User
from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "content",
            "created_by",
            "created_at",
            "updated_at",
        )
        extra_kwargs = {
            "created_by": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def save(self, **kwargs):
        self.validated_data["created_by"] = self.context["user"]
        return super().save(**kwargs)
