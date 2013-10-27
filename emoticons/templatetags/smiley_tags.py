"""Template tags for emoticons app"""
import re
import os

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from emoticons.settings import EMOTICONS_URL
from emoticons.settings import EMOTICONS_LIST
from emoticons.settings import EMOTICONS_CLASS

register = template.Library()

RE_EMOTICONS_LIST = [(re.compile(re.escape(emoticon[0])),
                      emoticon[0], emoticon[1])
                     for emoticon in EMOTICONS_LIST]


def replace_emoticons(content, autoescape=None):
    esc = autoescape and conditional_escape or (lambda x: x)
    content = esc(content)
    for emoticon, name, image in RE_EMOTICONS_LIST:
        if emoticon.search(content):
            emoticon_html = '<img class="%s" src="%s" alt="%s" />' % (
                EMOTICONS_CLASS, os.path.join(EMOTICONS_URL, image), name)
            content = emoticon.sub(emoticon_html, content)
    return mark_safe(content)
replace_emoticons.needs_autoescape = True


class SmileyNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return replace_emoticons(output)


def do_replace_emoticons(parser, token):
    nodelist = parser.parse(('endemoticons',))
    parser.delete_first_token()
    return SmileyNode(nodelist)


register.tag('emoticons', do_replace_emoticons)
register.filter('emoticons', replace_emoticons)
