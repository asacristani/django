from django.utils import timezone
import factory

from schedule.factories import ScheduleFactory
from task.models import Task
from user.factories import UserFactory


class TaskFactory(factory.django.DjangoModelFactory):
    content = factory.Faker('paragraph')
    schedule = factory.SubFactory(ScheduleFactory)

    class Meta:
        model = Task
