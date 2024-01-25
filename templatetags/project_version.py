from django import template

from gestao_ambiental.version import __version__

register = template.Library()


@register.simple_tag
def project_version():
    """Return package version as listed in `__version__` in `init.py`."""
    return __version__
