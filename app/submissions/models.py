from django.db import models
from django.utils.translation import gettext_lazy as _

from app.events.models import Event
from app.utils import fields as model_fields
from app.utils.models import BaseUUIDModel


class TextEmbedding(BaseUUIDModel):
    text = models.TextField(_("Text"), blank=False)
    embeddings = model_fields.ListField(_("Embeddings"))

    def __str__(self):
        return f"[ {self.id} ]: {self.text}"

    def create_event(self, operation="update"):
        Event.objects.create(
            type="form_embedding",
            data={
                "operation": operation,
                "id": str(self.id),
                "text": self.text,
                "embeddings": self.embeddings,
            },
        )


class FormSubmission(BaseUUIDModel):
    email = models.CharField(_("User Email"), blank=False, max_length=512)
    path = models.CharField(_("Path"), blank=False, max_length=1024)
    name = models.CharField(_("Name"), blank=False, max_length=255)
    type = models.CharField(_("Type"), blank=False, max_length=50)
    fields = model_fields.DictionaryField(_("Fields"))

    def __str__(self):
        return self.name

    def create_event(self, operation="update"):
        Event.objects.create(
            type="form_submission",
            data={
                "operation": operation,
                "id": str(self.id),
                "email": self.email,
                "path": self.path,
                "name": self.name,
                "type": self.type,
                "fields": self.fields,
            },
        )
        if operation != "delete":
            self.save()
