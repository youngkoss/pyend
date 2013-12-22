from django.contrib import admin
from dashboard.models import Dashboard


class DashboardAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dashboard, DashboardAdmin)