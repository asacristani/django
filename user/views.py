from datetime import datetime

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.models import User
from user.serializers import UserSerializer
from .utils import calculate_available_tasks


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def available_tasks_for_user_view(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        current_date = datetime.today().date()

        user_targets = [user]

        available_tasks = calculate_available_tasks(user_targets, current_date)
        if available_tasks:
            tasks_for_user = available_tasks[0][user]
            task_list = [{"id": task.id, "content": task.content} for task in tasks_for_user]
        else:
            task_list = []

        return Response(task_list, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
