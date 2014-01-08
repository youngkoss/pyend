from tastypie_resource.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from dashboard.api import DashboardResource
from notification.api import NotificationResource
from partner.api import PartnerResource

from user.models import User


class UserResource(ModelResource):
    dashboards = fields.ToManyField(DashboardResource, 'dashboards', null=True, blank=True,)
    notifications = fields.ToManyField(NotificationResource, 'notifications', null=True, blank=True,)
    partners = fields.ToManyField(PartnerResource, 'partners', null=True, blank=True,)

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()

        excludes = ['resource_uri']

    def dehydrate(self, bundle):
        bundle.data['task'] = []
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if hasattr(field, 'is_related') and field.is_related:
                bundle.data['task'].append({field.to.Meta.resource_name: field.to.get_resource_uri(field.to())})
        return bundle
