from datetime import timedelta
import random

from django.utils import timezone
import factory
import factory.fuzzy

from milestone.models import Milestone, UserMilestone
from user.factories import UserFactory


class MilestoneFactory(factory.django.DjangoModelFactory):
    slug = factory.fuzzy.FuzzyChoice(['invitation', 'registration'])

    class Meta:
        model = Milestone


class UserMilestoneFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    milestone = factory.SubFactory(MilestoneFactory)
    date = factory.Faker('date_this_year')

    class Meta:
        model = UserMilestone
