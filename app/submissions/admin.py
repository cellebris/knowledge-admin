from django.contrib import admin

from . import models


@admin.register(models.FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    pass
