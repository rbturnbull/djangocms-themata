from django import template
from django.utils.safestring import mark_safe

from djangocms_themata.models import Stylesheet

register = template.Library()

@register.inclusion_tag('themata/link.html')
def link_stylesheets():
    return {
        'stylesheets': Stylesheet.objects.filter(active=True),
    }