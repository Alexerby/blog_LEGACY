from django.contrib import admin
from .models import ContentSnippet

class ContentSnippetAdmin(admin.ModelAdmin):
    search_fields = ['ident', 'content']

admin.site.register(ContentSnippet, ContentSnippetAdmin)
