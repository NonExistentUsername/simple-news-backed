# Generated by Django 4.1.7 on 2023-03-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
