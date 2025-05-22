import private_storage.urls
from django.conf import settings
from django.urls import path
from drf_spectacular.views import SpectacularAPIView
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.api import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("event", views.EventViewSet)
router.register("user", views.UserViewSet)
router.register("team", views.TeamViewSet)
router.register("project", views.TeamProjectViewSet)
router.register("document_collection", views.TeamDocumentCollectionViewSet)
router.register("document", views.TeamDocumentViewSet)
router.register("media_collection", views.TeamMediaCollectionViewSet)
router.register("media", views.TeamMediaViewSet)
router.register("media_bookmark", views.TeamMediaBookmarkViewSet)
router.register("summary", views.ProjectSummaryViewSet)
router.register("note", views.ProjectNoteViewSet)
router.register("feedback", views.FeedbackViewSet)
router.register("form", views.FormSubmissionViewSet)
router.register("embedding", views.TextEmbeddingViewSet)
router.register("message", views.MessageViewSet)


# API URLS
app_name = "api"
urlpatterns = [
    path("status/", views.Status.as_view(), name="status"),
    path("", SpectacularAPIView.as_view(), name="api-schema"),
] + router.urls
