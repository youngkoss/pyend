from django.db import models
from user.models import User


class Partner(models.Model):
    user = models.ForeignKey(User, related_name='partners', null=True, blank=True)
    is_active = models.NullBooleanField(default=False, null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
