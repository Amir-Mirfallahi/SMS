from django import template

register = template.Library()


@register.filter
def iter_len(iterator):
    return len(iterator)
