from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LunarPhase(TimeStamp):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title