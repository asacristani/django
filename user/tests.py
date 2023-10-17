from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from user.models import User
from milestone.models import Milestone, UserMilestone
from schedule.models import Schedule
from task.models import Task
from user.utils import calculate_available_tasks


class CalculateAvailableTasksTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.milestone = Milestone.objects.create(slug='Invitation')
        self.user_milestone = UserMilestone.objects.create(user=self.user, milestone=self.milestone, date=date(2023, 1, 1))
        self.schedule = Schedule.objects.create(milestone=self.milestone, start_offset=timedelta(days=0), end_offset=timedelta(days=360))
        self.task = Task.objects.create(schedule=self.schedule, content='Description for Task 1')

    def test_calculate_available_tasks_ok(self):
        result = calculate_available_tasks([self.user], date(2023, 5, 6))

        self.assertEqual(1, len(result))
        self.assertIn('Task 1', result[0][self.user][0].content)

    def test_calculate_available_tasks_no_user(self):
        non_existent_user = User.objects.create(username='non_existent_user')
        result = calculate_available_tasks([non_existent_user], date(2023, 5, 6))

        self.assertEqual(0, len(result))

    def test_calculate_available_tasks_no_available_tasks(self):
        self.schedule.start_offset = timedelta(days=361)
        self.schedule.end_offset = timedelta(days=370)
        self.schedule.save()
        result = calculate_available_tasks([self.user], date(2023, 5, 6))

        self.assertEqual(0, len(result))

    def test_calculate_available_tasks_invalid_date(self):
        result = calculate_available_tasks([self.user], date(2022, 5, 6))

        self.assertEqual(0, len(result))


class AvailableTasksForUserViewTestCase(TestCase):
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
        self.user_milestone = UserMilestone.objects.create(
            user=self.user,
            milestone=self.milestone,
            date=date.today() - timedelta(days=5)
        )

    def test_available_tasks_for_user_view(self):
        url = reverse('available-tasks-for-user', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {
                "id": self.task.id,
                "content": self.task.content
            }
        ]
        self.assertEqual(response.data, expected_data)

    def test_available_tasks_for_user_view_user_not_found(self):
        url = reverse('available-tasks-for-user', args=[999])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "User not found"})

    def test_available_tasks_for_user_view_no_available_tasks(self):
        self.task.schedule.start_offset = timedelta(days=361)
        self.task.schedule.end_offset = timedelta(days=370)
        self.task.schedule.save()

        url = reverse('available-tasks-for-user', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
