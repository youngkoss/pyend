from tastypie.resources import ModelResource
from notification.models import Notification
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields


class NotificationResource(ModelResource):
    user = fields.ToOneField('user.api.UserResource', 'user', null=True, blank=True)

    class Meta:
        queryset = Notification.objects.all()
        resource_name = 'notification'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()

    def determine_format(self, request):
        return 'application/json'