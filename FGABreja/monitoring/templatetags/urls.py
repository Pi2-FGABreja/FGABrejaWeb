from django import template
from django.conf import settings

register = template.Library()


@register.assignment_tag
def insert_malt_url():
    url = settings.API_URL
    return url + "insert/malt/"


@register.assignment_tag
def iodine_test_url():
    url = settings.API_URL
    return url + "iodine/test/"
