from tastypie_resource.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from notification.models import Notification


class NotificationResource(ModelResource):
    user = fields.ToOneField('user.api.UserResource', 'user', null=True, blank=True)

    class Meta:
        queryset = Notification.objects.all()
        resource_name = 'notification'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()

