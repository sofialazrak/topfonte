from django import template

register = template.Library()

@register.filter
def lookup(d, key):
    return d[key]

@register.filter
def list_item(lst, i):
    try:
        return lst[i]
    except:
        return None