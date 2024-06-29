from django.contrib import admin
from user.admin import admin_site

from .models import ContentSnippet

class ContentSnippetAdmin(admin.ModelAdmin):
    search_fields = ['ident', 'content']

admin_site.register(ContentSnippet, ContentSnippetAdmin)
