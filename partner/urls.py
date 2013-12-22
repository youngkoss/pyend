from tastypie.api import Api
from partner.api import PartnerResource


v1_api = Api(api_name='v1')
v1_api.register(PartnerResource)

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
