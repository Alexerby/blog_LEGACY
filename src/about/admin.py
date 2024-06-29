from django.contrib import admin
from .models import AboutSection, WorkReference

from user.admin import admin_site

admin_site.register(AboutSection)
admin_site.register(WorkReference)
