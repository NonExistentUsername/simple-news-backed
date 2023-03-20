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
    created_at = models.DateTimeField(
        auto_now_add=datetime.datetime.now,
    )
