from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email']
    readonly_fields = ['password']


admin.site.register(User, UserAdmin)
