from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Au31appViewSet

router = DefaultRouter()
router.register("au31app", Au31appViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
