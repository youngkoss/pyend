from django.db import models
from user.models import User


class Dashboard(models.Model):
    user = models.ForeignKey(User, related_name='dashboards', null=True, blank=True)
    is_active = models.NullBooleanField(default=False, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    is_done = models.NullBooleanField(null=True, blank=True)
    approve = models.NullBooleanField(null=True, blank=True)