"""Template tags for emoticons app"""
from bs4 import BeautifulSoup

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from emoticons.settings import EMOTICONS_LIST
from emoticons.settings import EMOTICONS_COMPILED

register = template.Library()


def regexp_replace_emoticons(content):
    """
    Replace the emoticons string by HTML images,
    with regular expressions.
    """
    for emoticon, emoticon_html in EMOTICONS_COMPILED:
        if emoticon.search(content):
            content = emoticon.sub(emoticon_html, content)
    return content


def replace_emoticons(content, excluded_markups):
    """
    Replace the emoticons string by HTML images.
    If some markups should be excluded from replacement,
    BeautifulSoup will be used.
    """
    if not excluded_markups:
        return regexp_replace_emoticons(content)

    excluded_markups = excluded_markups.split(',') + ['[document]']
    soup = BeautifulSoup(content, 'html.parser')

    for content_string in list(soup.strings):
        if content_string.parent.name not in excluded_markups:
            replaced_content_string = regexp_replace_emoticons(content_string)
            if content_string != replaced_content_string:
                content_string.replace_with(
                    BeautifulSoup(replaced_content_string, 'html.parser'))
    return str(soup)


class EmoticonNode(template.Node):
    """
    Node for applying ``replace_emoticons`` on content.
    """
    def __init__(self, nodelist, exclude):
        self.nodelist = nodelist
        self.exclude = exclude
        if exclude:
            self.exclude_var = template.Variable(exclude)

    def render(self, context):
        content = self.nodelist.render(context)

        exclude = self.exclude
        if exclude:
            if exclude[0] == exclude[-1] and exclude[0] in ("'", '"'):
                exclude = exclude[1:-1]
            else:
                exclude = self.exclude_var.resolve(context)

        return replace_emoticons(content, exclude)


@register.tag('emoticons')
def emoticons_tag(parser, token):
    """
    Tag for rendering emoticons.
    """
    exclude = ''
    args = token.split_contents()
    if len(args) == 2:
        exclude = args[1]
    elif len(args) > 2:
        raise template.TemplateSyntaxError(
            'emoticons tag has only one optional argument')

    nodelist = parser.parse(['endemoticons'])
    parser.delete_first_token()
    return EmoticonNode(nodelist, exclude)


@register.filter('emoticons', needs_autoescape=True)
def emoticons_filter(content, exclude='', autoescape=None):
    """
    Filter for rendering emoticons.
    """
    esc = autoescape and conditional_escape or (lambda x: x)
    content = mark_safe(replace_emoticons(esc(content), exclude))
    return content


@register.assignment_tag
def emoticons_index():
    """
    Display an tuple of list of available emoticons.
    """
    return list(zip(*EMOTICONS_LIST))[0]
