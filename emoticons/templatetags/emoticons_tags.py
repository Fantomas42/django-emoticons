"""Template tags for emoticons app"""
import os
import binascii

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from emoticons.settings import EMOTICONS_LIST
from emoticons.settings import EMOTICONS_REGEXP
from emoticons.settings import EMOTICONS_DIRECTORY

register = template.Library()

EMOTICON_TEMPLATE = template.loader.get_template('emoticons/emoticon.html')


def replace_emoticons(content):
    """
    Replace the emoticons string by HTML images.
    """
    for emoticon, name, image in EMOTICONS_REGEXP:
        if emoticon.search(content):
            context = template.Context({
                'name': name,
                'code': binascii.hexlify(name.encode('utf-8')),
                'image': os.path.join(EMOTICONS_DIRECTORY, image)})
            emoticon_html = EMOTICON_TEMPLATE.render(context).strip()
            content = emoticon.sub(emoticon_html, content)
    return content


class EmoticonNode(template.Node):
    """
    Node for applying ``replace_emoticons`` on content.
    """
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        return replace_emoticons(content)


@register.tag('emoticons')
def emoticons_tag(parser, token):
    """
    Tag for rendering emoticons.
    """
    nodelist = parser.parse(['endemoticons'])
    parser.delete_first_token()
    return EmoticonNode(nodelist)


@register.filter('emoticons', needs_autoescape=True)
def emoticons_filter(content, autoescape=None):
    """
    Filter for rendering emoticons.
    """
    esc = autoescape and conditional_escape or (lambda x: x)
    content = mark_safe(replace_emoticons(esc(content)))
    return content


@register.assignment_tag
def emoticons_index():
    """
    Display an tuple of list of available emoticons.
    """
    return zip(*EMOTICONS_LIST)[0]
