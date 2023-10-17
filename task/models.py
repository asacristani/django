from django.db import models

from user.models import User
from schedule.models import Schedule


class Task(models.Model):
    content = models.TextField()
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.content + ":" + str(self.schedule)
