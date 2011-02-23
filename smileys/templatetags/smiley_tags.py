"""Template tags for smileys app"""
import re
import os

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from smileys.settings import SMILEYS_URL
from smileys.settings import SMILEYS_LIST
from smileys.settings import SMILEYS_CLASS

register = template.Library()

RE_SMILEYS_LIST = [(re.compile(re.escape(smiley[0])), smiley[0], smiley[1])
                   for smiley in SMILEYS_LIST]


def replace_smileys(content, autoescape=None):
    esc = autoescape and conditional_escape or (lambda x: x)

    for smiley, name, image in RE_SMILEYS_LIST:
        if smiley.search(content):
            smiley_html = '<img class="%s" src="%s" alt="%s" />' % (
                SMILEYS_CLASS, os.path.join(SMILEYS_URL, image), name)
            content = smiley.sub(smiley_html, esc(content))
    return mark_safe(content)
replace_smileys.needs_autoescape = True


class SmileyNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return replace_smileys(output)


def do_replace_smileys(parser, token):
    nodelist = parser.parse(('endsmileys',))
    parser.delete_first_token()
    return SmileyNode(nodelist)


register.tag('smileys', do_replace_smileys)
register.filter('smileys', replace_smileys)
