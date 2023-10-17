from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.


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
