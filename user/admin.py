from django.contrib import admin
from user.models import User
from django.contrib.auth.models import User as DjangoUser

admin.site.unregister(DjangoUser)


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)