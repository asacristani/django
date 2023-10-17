from datetime import date

from user.models import User
from milestone.models import UserMilestone
from schedule.models import Schedule
from task.models import Task


def calculate_available_tasks(user_targets: [User], date_target: date):
    """ Calculate available tasks for a user in a date """
    available_tasks = []

    # 1. Get all Milestones for the user target WHERE date >= date_target
    user_milestones = UserMilestone.objects.filter(user__in=user_targets, date__lte=date_target)

    # 2. Get all Schedules for the Milestones WHERE offset (date_target - date) between offset range
    for user_milestone in user_milestones:
        milestone = user_milestone.milestone
        schedules = Schedule.objects.filter(
            milestone=milestone,
            start_offset__lte=date_target - user_milestone.date,
            end_offset__gte=date_target - user_milestone.date
        )

        # 3. Get all Tasks for the Schedules
        for schedule in schedules:
            tasks = Task.objects.filter(schedule=schedule)
            available_tasks.append({user_milestone.user: tasks})

    return available_tasks

# from calculate_available_tasks import calculate_available_tasks
# from milestone.models import UserMilestone
# from datetime import date
# user = UserMilestone.objects.all()[10].user
# calculate_available_tasks(user, date(2023,5,6))
