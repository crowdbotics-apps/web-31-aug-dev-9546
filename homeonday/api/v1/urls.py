from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Mayh9jiusViewSet

router = DefaultRouter()
router.register("mayh9jius", Mayh9jiusViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
