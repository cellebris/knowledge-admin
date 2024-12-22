# Generated by Django 4.2.5 on 2024-05-18 08:00

import app.utils.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Team Name")),
                ("summary_prompt", models.TextField(default="", verbose_name="Summarization instructions")),
                (
                    "format_prompt",
                    models.TextField(
                        default="\nGenerate an engaging summary on the topic with appropriate headings, subheadings, paragraphs, and bullet points.\n    ",
                        verbose_name="Format instructions",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamInvite",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                ("email", models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="TeamTag",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Team Tags")),
                (
                    "team",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="tags", to="teams.team"),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamMembership",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                ("settings", app.utils.fields.DictionaryField(default=dict, verbose_name="User Settings")),
                (
                    "team",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="members", to="teams.team"),
                ),
            ],
        ),
    ]
