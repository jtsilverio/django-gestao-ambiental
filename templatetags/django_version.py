import django
from django import template

register = template.Library()


@register.simple_tag
def django_version():
    """Template tag to get the current Django version.

    Returns:
        str: The current Django version.
    """
    return django.get_version()
