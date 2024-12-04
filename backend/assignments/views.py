from django.db import transaction

from rest_framework import viewsets
from rest_framework.exceptions import APIException

# from assignments.models import Assignment
# from assignments.serializers import AssignmentSerializer
from assignments.tasks import long_running_task, task1, task2

from django.http import JsonResponse
from django.views.decorators.http import require_GET

from django.db import connections
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from django.db.utils import OperationalError

class DatabaseConnectionViewSet(viewsets.ViewSet):
    """
    ViewSet to check if the database is connected.
    This ViewSet will return the status of the database connection.
    """

    @action(detail=False, methods=['get'], url_path='check-db')
    def check_db_connection(self, request):
        """
        API action to check if the MySQL database is connected to Django.
        Returns a JSON response with the database connection status.
        """
        try:
            # Ensure you're using the correct connection alias (typically 'default' in Django settings)
            connection = connections['default']  # Use the default connection alias
            connection.ensure_connection()  # Ensure the connection is established
            connection.close()  # Close the connection after checking
            
            return Response({
                'status': 'success',
                'message': 'Database connected successfully'
            }, status=HTTP_200_OK)

        except OperationalError as e:
            # In case of a connection error, return error details in the response
            return Response({
                'status': 'error',
                'message': f'Database connection failed: {str(e)}'
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)

class PdfUploadViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path='upload')
    def upload(self, request):
        long_running_task.delay()
        return JsonResponse({"message": "Task has been started!"})
    
class Task1ViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path='task1')
    def upload(self, request):
        task1.delay()
        return JsonResponse({"message": "Task1 has been started!"})


class Task2ViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'], url_path='task2')
    def upload(self, request):
        task2.delay()
        return JsonResponse({"message": "Task2 has been started!"})



@require_GET
def check_db_connection(request):
    """
    API to check if the MySQL database is connected to Django.
    Returns a JSON response with the database connection status.
    """
    try:
        # Try to make a connection to the database
        connection = connections['mydb']
        connection.ensure_connection()  # Ensure the connection is established
        connection.close()  # Close the connection after checking
        
        return JsonResponse({
            'status': 'success',
            'message': 'Database connected successfully'
        }, status=200)

    except OperationalError as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Database connection failed: {str(e)}'
        }, status=500)