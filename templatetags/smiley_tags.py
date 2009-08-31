"""Template tags for smileys app"""
from os.path import join

from django import template
from django.template.defaultfilters import stringfilter

from smileys.settings import SMILEYS_URL
from smileys.settings import SMILEYS_LIST
from smileys.settings import SMILEYS_CLASS

register = template.Library()

@stringfilter
def replace_smileys(value):
    for pattern, image in SMILEYS_LIST:
        if pattern in value:
            smiley_html = '<img class="%s" src="%s" alt="%s" />' % (
                SMILEYS_CLASS, join(SMILEYS_URL, image), pattern)
            value = value.replace(pattern, smiley_html)
    return value

register.filter('smileys', replace_smileys)
replace_smileys.is_safe = True
