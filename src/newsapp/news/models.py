import datetime

from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=63,
    )
    content = models.TextField(
        max_length=4095,
    )

    created_by = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(
        auto_now=datetime.datetime.now,
    )
    created_at = models.DateTimeField(
        auto_now_add=datetime.datetime.now,
    )
    is_published = models.BooleanField(
        default=False,
    )
    is_banned = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["-created_at"]
