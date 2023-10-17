from django.core.management.base import BaseCommand

from milestone.factories import MilestoneFactory, UserMilestoneFactory
from schedule.factories import ScheduleFactory
from task.factories import TaskFactory
from user.factories import UserFactory


class Command(BaseCommand):
    help = 'Generate sample scheduling data.'

    def handle(self, *args, **kwargs):
        schedules = ScheduleFactory.create_batch(50)
        invitation = MilestoneFactory(slug='invitation')
        registration = MilestoneFactory(slug='registration')

        for schedule in schedules:
            TaskFactory(schedule=schedule)
            TaskFactory(schedule=schedule)

        for idx, schedule in enumerate(schedules):
            print(f'Generating data for schedule {idx + 1} of {len(schedules)}')
            UserMilestoneFactory.create_batch(500, milestone__slug=invitation)
            UserMilestoneFactory.create_batch(500, milestone__slug=registration)
