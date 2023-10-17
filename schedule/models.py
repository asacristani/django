from django.db import models

from milestone.models import Milestone


class Schedule(models.Model):
    milestone = models.ForeignKey(Milestone, on_delete=models.PROTECT)
    start_offset = models.DurationField()
    end_offset = models.DurationField()
