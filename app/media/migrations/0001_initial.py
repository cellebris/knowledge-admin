# Generated by Django 5.0.7 on 2024-12-01 18:13

import app.media.models
import django.db.models.deletion
import private_storage.fields
import private_storage.storage.files
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("teams", "0003_remove_team_format_prompt_remove_team_summary_prompt"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamMediaCollection",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Media Collection Name")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="The images in this media collection are used by the publishing AI to match relevant images with data cards.  This description will help the recommendation engine find appropriate images for site content.",
                        verbose_name="Media Collection Description",
                    ),
                ),
                ("processed_time", models.DateTimeField(blank=True, null=True, verbose_name="Processed Time")),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="media_collections", to="teams.team"
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamMediaBookmark",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="The images in this media collection are used by the publishing AI to match relevant images with data cards.  This description will help the recommendation engine find appropriate images for site content.",
                        verbose_name="Media Description",
                    ),
                ),
                ("url", models.URLField(max_length=500, verbose_name="URL")),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookmarks",
                        to="media.teammediacollection",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamMedia",
            fields=[
                ("created", models.DateTimeField(editable=False)),
                ("updated", models.DateTimeField(editable=False)),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="The images in this media collection are used by the publishing AI to match relevant images with data cards.  This description will help the recommendation engine find appropriate images for site content.",
                        verbose_name="Media Description",
                    ),
                ),
                (
                    "file",
                    private_storage.fields.PrivateFileField(
                        storage=private_storage.storage.files.PrivateFileSystemStorage(),
                        upload_to=app.media.models.team_media_path,
                        verbose_name="Image File",
                    ),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="files",
                        to="media.teammediacollection",
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
                "abstract": False,
            },
        ),
    ]
