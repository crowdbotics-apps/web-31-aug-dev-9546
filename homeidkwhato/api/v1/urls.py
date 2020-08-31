from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HesoyamViewSet

router = DefaultRouter()
router.register("hesoyam", HesoyamViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
