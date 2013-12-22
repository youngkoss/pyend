from tastypie.resources import ModelResource
from dashboard.models import Dashboard
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields


class DashboardResource(ModelResource):
    user = fields.ToOneField('user.api.UserResource', 'user', null=True, blank=True)

    class Meta:
        queryset = Dashboard.objects.all()
        resource_name = 'dashboard'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()

    def determine_format(self, request):
        return 'application/json'