from django import template
from django.forms import CheckboxInput
from django.forms import ClearableFileInput
from django.forms import FileInput

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    original_classes = field.field.widget.attrs.get('class')
    original_classes = original_classes + ' ' if original_classes else ''

    disallow =[
        FileInput().__class__.__name__,
        CheckboxInput().__class__.__name__,
        ClearableFileInput().__class__.__name__
    ]

    if field.field.widget.__class__.__name__ in disallow:
        css = css.replace("form-control", "")
        return field.as_widget(attrs={"class": original_classes + css})
    return field.as_widget(attrs={"class": original_classes + css})


@register.filter
def is_false(arg):
    """Differentiates False from None."""

    return arg is False
