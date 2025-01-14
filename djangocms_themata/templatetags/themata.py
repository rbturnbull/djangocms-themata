from django import template
from django.utils.safestring import mark_safe

from djangocms_themata.models import Stylesheet
from djangocms_themata.util import load_stylesheets

register = template.Library()

@register.inclusion_tag('themata/link.html')
def link_stylesheets():
    stylesheets = Stylesheet.objects.filter(active=True)
    if not stylesheets:
        stylesheets = Stylesheet.objects.filter(name="Cosmo")

    return {'stylesheets': stylesheets}