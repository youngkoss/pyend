from tastypie.resources import ModelResource
from partner.models import Partner
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields


class PartnerResource(ModelResource):
    user = fields.ToOneField('user.api.UserResource', 'user', null=True, blank=True)

    class Meta:
        queryset = Partner.objects.all()
        resource_name = 'partner'

        # authorization = DjangoAuthorization()
        # authentication = BasicAuthentication()

    def determine_format(self, request):
        return 'application/json'