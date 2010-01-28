"""Template tags for smileys app"""
from os.path import join

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

from smileys.settings import SMILEYS_URL
from smileys.settings import SMILEYS_LIST
from smileys.settings import SMILEYS_CLASS

register = template.Library()

def replace_smileys(content, autoescape=None):
    esc = autoescape and conditional_escape or (lambda x: x)

    for pattern, image in SMILEYS_LIST:
        if pattern in content:
            smiley_html = '<img class="%s" src="%s" alt="%s" />' % (
                SMILEYS_CLASS, join(SMILEYS_URL, image), pattern)
            content = esc(content).replace(pattern, smiley_html)
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

