from tastypie_resource.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from dashboard.models import Dashboard


class DashboardResource(ModelResource):
    user = fields.ToOneField('user.api.UserResource', 'user', null=True, blank=True)

    class Meta:
        queryset = Dashboard.objects.all()
        resource_name = 'dashboard'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()
