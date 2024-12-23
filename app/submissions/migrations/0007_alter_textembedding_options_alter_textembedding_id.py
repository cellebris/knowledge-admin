# Generated by Django 5.0.7 on 2024-11-28 07:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submissions", "0006_remove_textembedding_embedding_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="textembedding",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterField(
            model_name="textembedding",
            name="id",
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
