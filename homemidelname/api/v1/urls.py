from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HuskywhitecolourViewSet

router = DefaultRouter()
router.register("huskywhitecolour", HuskywhitecolourViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
