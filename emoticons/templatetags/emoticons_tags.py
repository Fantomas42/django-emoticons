"""Template tags for emoticons app"""
from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from emoticons.settings import EMOTICONS_LIST
from emoticons.settings import EMOTICONS_COMPILED

register = template.Library()


def replace_emoticons(content):
    """
    Replace the emoticons string by HTML images.
    """
    for emoticon, emoticon_html in EMOTICONS_COMPILED:
        if emoticon.search(content):
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
    return list(zip(*EMOTICONS_LIST))[0]
