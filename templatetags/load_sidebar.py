from django import template

from gestao_ambiental import sidebar

register = template.Library()


@register.simple_tag(takes_context=True)
def load_sidebar(context):
    """Django template tag that loads the sidebar menu into the context.

    This function takes the current template context and adds the sidebar menu
    to it. This allows the sidebar menu to be accessed directly in the template.

    Args:
        context (dict): The current template context.

    Returns:
        str: An empty string. In Django, simple tags must return a string
             that will be inserted into the template where the tag is used.
             Since this function is only used for its side effect of modifying
             the context, it returns an empty string.
    """
    context["sidebar"] = sidebar.MENU_SIDEBAR
    return ""
