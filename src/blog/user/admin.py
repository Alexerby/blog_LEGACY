from django.contrib import admin

from .models import User, CustomGroup

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    readonly_fields = ['password']


admin.site.register(User, UserAdmin)


from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

admin.site.unregister(Group)

@admin.register(CustomGroup)
class CustomGroupAdmin(GroupAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'permissions')}),
        (_('Description'), {'fields': ('description',)}),
    )
