from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ModelViewSet

router = DefaultRouter()
router.register("model", ModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
