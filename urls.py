from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings

from tastypie.api import Api
from dashboard.api import DashboardResource
from partner.api import PartnerResource
from notification.api import NotificationResource
from user.api import UserResource

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PyEnd.views.home', name='home'),
    # url(r'^PyEnd/', include('PyEnd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(DashboardResource())
v1_api.register(PartnerResource())
v1_api.register(NotificationResource())

urlpatterns += patterns('',
                        (r'^api/', include(v1_api.urls)),
                        )
