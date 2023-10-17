from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from task.models import Task
from task.serializers import TaskSerializer
from user.models import User


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def users_for_task_view(request, task_id):
    try:
        task = Task.objects.get(id=task_id)

        milestone = task.schedule.milestone
        users = User.objects.filter(usermilestone__milestone=milestone)

        user_list = [{"id": user.id, "username": user.username} for user in users]
        return Response(user_list, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
