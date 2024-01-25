# https://stackoverflow.com/questions/3927018/django-how-to-check-if-field-widget-is-checkbox-in-the-template
# https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
from django import template
from django.forms import CheckboxSelectMultiple

register = template.Library()


@register.filter(name="is_multiple_choice")
def is_multiple_choice(field):
    """Template filter to check if a form field is a CheckboxSelectMultiple.

    Args:
        field (forms.Field): Django form field.

    Returns:
        bool: True if the field's widget is CheckboxSelectMultiple, False otherwise.
    """
    return isinstance(field.field.widget, CheckboxSelectMultiple)
