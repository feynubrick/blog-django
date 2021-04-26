from django.template import Library
from django.template.defaultfilters import stringfilter

import markdown as md

register = Library()

@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=['markdown.extensions.fenced_code'])