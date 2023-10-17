from datetime import timedelta
import random

from django.utils import timezone
import factory

from milestone.factories import MilestoneFactory
from schedule.models import Schedule


class ScheduleFactory(factory.django.DjangoModelFactory):
    milestone = factory.SubFactory(MilestoneFactory)
    start_offset = timedelta(days=random.randint(-365, 365))
    end_offset = factory.LazyAttribute(lambda o: o.start_offset + timedelta(days=random.randint(-365, 365)))

    class Meta:
        model = Schedule
