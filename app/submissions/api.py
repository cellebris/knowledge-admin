import time
from datetime import datetime

from app.api import permissions, views

from . import models


#
# Update Handler
#
def create_form_event(self, instance):
    instance.create_event()


def create_embedding_event(self, instance):
    if not instance.embeddings:
        instance.create_event()
        start_time = datetime.now()
        while (datetime.now() - start_time).seconds < 100:
            embedding_test = models.TextEmbedding.objects.get(id=instance.id)
            if embedding_test.embeddings:
                instance.embeddings = embedding_test.embeddings
                break
            time.sleep(0.5)


#
# Model Endpoints
#
views.generate(
    models.TextEmbedding,
    permission_classes=[permissions.EnginePermissions],
    filter_fields={
        "id": "id",
        "text": "long_text",
        "created": "date_time",
        "updated": "date_time",
    },
    ordering_fields=["created"],
    search_fields=["text"],
    view_fields=[
        "id",
        "text",
        "embeddings",
        "created",
        "updated",
    ],
    create_fields=[
        "text",
        ("embeddings", {"read_only": True}),
    ],
    update_fields=[
        "embeddings",
    ],
    handler=create_embedding_event,
)


views.generate(
    models.FormSubmission,
    permission_classes=[permissions.EnginePermissions],
    filter_fields={
        "id": "id",
        "email": "id",
        "path": "short_text",
        "name": "short_text",
        "type": "short_text",
        "created": "date_time",
        "updated": "date_time",
    },
    ordering_fields=["created", "name", "type", "email", "path"],
    search_fields=["name", "type", "email", "path"],
    view_fields=[
        "id",
        "email",
        "path",
        "name",
        "type",
        "fields",
        "created",
        "updated",
    ],
    create_fields=[
        "email",
        "path",
        "name",
        "type",
        "fields",
    ],
    update_fields=[],
    handler=create_form_event,
)
