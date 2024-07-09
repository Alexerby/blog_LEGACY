from django.contrib import admin

from user.admin import admin_site

from .models import BoatListing, Engine, Picture

admin_site.register(Engine)
admin_site.register(BoatListing)
admin_site.register(Picture)


