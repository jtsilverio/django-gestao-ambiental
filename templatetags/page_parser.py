# https://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template
# https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
from django import template

register = template.Library()


@register.simple_tag
def page_parser(field_name, value, urlencode=None):
    """Django template tag that generates a URL with updated query parameters.

    This function takes a field name and a value, and optionally a URL-encoded
    string of current query parameters. It generates a new URL that includes
    the field name and value as a query parameter, and also includes all other
    existing query parameters except for the one with the same field name.

    Args:
        field_name (str): The name of the field to be added or updated in the query parameters.
        value (str): The value for the field.
        urlencode (str, optional): A URL-encoded string of the current query parameters.

    Returns:
        str: A URL that includes the new field and value as a query parameter,
             and all other existing query parameters except for the one with the same field name.
    """
    url = f"?{field_name}={value}"

    if urlencode:
        query_list = urlencode.split("&")
        filtered_query_list = filter(
            lambda p: p.split("=")[0] != field_name, query_list
        )
        query_for_other_fields = "&".join(filtered_query_list)

        url = f"{url}&{query_for_other_fields}"

    return url
