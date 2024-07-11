from django.contrib import admin

from user.admin import admin_site

from .models import BoatListing, Engine, Picture, Overview, Dimension, Construction

class OverviewInline(admin.StackedInline):
    model = Overview
    extra = 0
    max_num = 1

class DimensionInline(admin.StackedInline):
    model = Dimension
    extra = 0
    max_num = 1

class ConstructionInline(admin.StackedInline):
    model = Construction
    extra = 0
    max_num = 1

class EngineInline(admin.StackedInline):
    model = Engine
    extra = 0
    max_num = 1

class PictureInline(admin.StackedInline):
    model = Picture
    max_num = 8

class BoatListingAdmin(admin.ModelAdmin):
    inlines = [OverviewInline, DimensionInline, ConstructionInline, EngineInline, PictureInline]


admin_site.register(BoatListing, BoatListingAdmin)
