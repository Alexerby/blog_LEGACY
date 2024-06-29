from user.admin import admin_site

from .models import Article

admin_site.register(Article)
