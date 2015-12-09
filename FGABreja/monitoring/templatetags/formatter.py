from django import template

register = template.Library()


@register.assignment_tag
def process_status_icon(is_active):
    if is_active:
        return "chevron_right"
    else:
        return "check"
