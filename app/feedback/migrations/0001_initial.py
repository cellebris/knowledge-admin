# Generated by Django 4.2.5 on 2024-05-18 08:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                ("path", models.CharField(max_length=1024, verbose_name="Page Path")),
                ("rating", models.IntegerField(verbose_name="Feedback Rating")),
                ("message", models.TextField(verbose_name="Feedback Message")),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
    ]
