from django import template

register = template.Library()

@register.filter
def get_verbose_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name.title()

@register.filter
def get_field_value(instance, field_name):
    return getattr(instance, field_name)

