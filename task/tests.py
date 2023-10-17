from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient

from user.models import User
from milestone.models import Milestone
from schedule.models import Schedule
from task.models import Task


class TaskModelTestCase(TestCase):
    def test_time_spent_is_initially_calculated_from_session_start_and_end_time(self):
        self.fail()

    def test_time_spent_is_updated_when_session_start_time_and_end_time_have_been_updated(self):
        self.fail()


class TaskAPITestCase(APITestCase):
    def test_staff_users_can_only_see_their_tasks(self):
        self.fail()

    def test_admin_users_can_see_all_tasks(self):
        self.fail()


class UsersForTaskViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(username='test_user')
        self.milestone = Milestone.objects.create(slug='Invitation')
        self.schedule = Schedule.objects.create(
            milestone=self.milestone,
            start_offset=timedelta(days=0),
            end_offset=timedelta(days=360)
        )
        self.task = Task.objects.create(schedule=self.schedule, content='Description for Task 1')

        self.user.usermilestone_set.create(milestone=self.milestone, date=date.today() - timedelta(days=5))

    def test_users_for_task_view(self):
        url = reverse('users-for-task', args=[self.task.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [{"id": self.user.id, "username": self.user.username}]
        self.assertEqual(response.data, expected_data)

    def test_users_for_task_view_task_not_found(self):
        url = reverse('users-for-task', args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Task not found"})
