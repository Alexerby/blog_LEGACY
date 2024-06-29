
# Admin config
from django.contrib import admin
from django_otp.admin import OTPAdminSite

# Models
from .models import User, CustomGroup
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import Group

# Misc
# from django.utils.translation import gettext_lazy as _



# OTP Admin - site setup
class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name='OTPAdmin')


# Register

## User
admin_site.register(User)
admin_site.register(TOTPDevice)

## Group
admin.site.unregister(Group)
admin_site.register(CustomGroup)


# Models
class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    readonly_fields = ['password']




