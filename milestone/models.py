from django.db import models

from user.models import User


class Milestone(models.Model):
    slug = models.SlugField()


class UserMilestone(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
