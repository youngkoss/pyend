from django.db import models
from datetime import datetime
from user.models import User


class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', null=True, blank=True)
    is_active = models.NullBooleanField(default=False, null=True, blank=True)
    date = models.DateField(default=datetime.now(), null=True, blank=True)
    description = models.TextField(null=True, blank=True)