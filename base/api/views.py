from .serializers import TaskSerializer
from base.models import Task, Tag
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def api_overview(request):
    """
    Get an overview of available API endpoints.
    """
    api_urls = {
        'Create': '/task-create/',
        'Read One': '/task-detail/<str:pk>/',
        'Read All': '/task-list/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    """
    Get a list of all tasks.
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    """
    Get details of a specific task by ID.
    """
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def task_create(request):
    """
    Create a new task.
    """
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        task = serializer.save()
        # Handle many-to-many relationship for tags
        tags_data = request.data.get('tags')
        if tags_data:
            for tag_data in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                task.tags.add(tag)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def task_update(request, pk):
    """
    Update an existing task by ID.
    """
    try: 
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data, partial=True)
        if serializer.is_valid():
            updated_task = serializer.save()
            # Handle many-to-many relationship for tags
            tags_data = request.data.get('tags')
            if tags_data:
                task.tags.clear()  # Clear existing tags
                for tag_data in tags_data:
                    tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
                    updated_task.tags.add(tag)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def task_delete(request, pk):
    """
    Delete a task by ID.
    """
    try: 
        task = Task.objects.get(id=pk)
        task.delete()
        return Response('Item successfully deleted!')
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
