from django.contrib.auth.models import User
from news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        read_only=True,
    )

    class Meta:
        model = News
        fields = (
            "id",
            "title",
            "content",
            "created_by",
            "created_at",
        )
        extra_kwargs = {"created_by": {"read_only": True}}

    def save(self, **kwargs):
        self.validated_data["created_by"] = self.context["user"]
        return super().save(**kwargs)
