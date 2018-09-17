from django.db import models
from django.utils import timezone


class UserInfo(models.Model):

    user_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
