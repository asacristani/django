from django.test import TestCase
from datetime import date, timedelta
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
