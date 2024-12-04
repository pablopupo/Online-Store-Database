from django import template
import base64

register = template.Library()

@register.filter
def base64encode(value):
    """
    Converts byte data to base64 string
    """
    return base64.b64encode(value).decode('utf-8')