from django.urls import re_path, path
from rest_framework.routers import DefaultRouter

from assignments.views import DatabaseConnectionViewSet, PdfUploadViewSet  
from django.urls import path, include
# Create the router for the existing viewset
router = DefaultRouter()
# router.register(r"assignments", AssignmentViewSet, basename="assignments")
router.register(r'db-status', DatabaseConnectionViewSet, basename='db-status')
router.register(r'upload', PdfUploadViewSet, basename='upload')

# Define the URL patterns for the API
# assignments_urlpatterns = router.urls

# Add the new API endpoint for checking the DB connection

urlpatterns = [
    path('api/', include(router.urls)),
]
assignments_urlpatterns = urlpatterns