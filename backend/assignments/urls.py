from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from assignments.views import DatabaseConnectionViewSet, PdfUploadViewSet, Task1ViewSet, Task2ViewSet
from django.urls import path, include

router = DefaultRouter()

router.register(r'db-status', DatabaseConnectionViewSet, basename='db-status')
router.register(r'upload', PdfUploadViewSet, basename='upload')
router.register(r'task1', Task1ViewSet, basename='task1')
router.register(r'task2', Task2ViewSet, basename='task2')

urlpatterns = [
    path('api/', include(router.urls)),
]
assignments_urlpatterns = urlpatterns