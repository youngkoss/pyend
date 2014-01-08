from tastypie_resource.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields

from partner.models import Partner


class PartnerResource(ModelResource):
    user = fields.ToOneField('user.api.UserResource', 'user', null=True, blank=True)

    class Meta:
        queryset = Partner.objects.all()
        resource_name = 'partner'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()
