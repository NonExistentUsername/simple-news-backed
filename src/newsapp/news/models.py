from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=63,
    )
    content = models.TextField(
        max_length=4095,
    )
