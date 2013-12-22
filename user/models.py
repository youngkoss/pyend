from django.db import models
from pytils.translit import slugify
# Create your models here.


class User(models.Model):
    is_active = models.NullBooleanField(default=True, null=True, blank=True)
    name_organization = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='image_logo', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.logo:
            self.logo.name = "{}.{}".format(slugify(self.logo.name.split('.')[0]), self.logo.name.split('.')[-1])
        super(User, self).save(*args, **kwargs)
