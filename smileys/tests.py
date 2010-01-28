"""Test for smileys app"""
import unittest

from django.template import Context, Template
#from smileys.templatetags.smiley_tags import replace_smileys

class SmileysTestCase(unittest.TestCase):

    def test_filter(self):
        t = Template("""
        {% load smiley_tags %}
        {{ content|smileys }}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertTrue("Coding is fun <img class=\"smiley\" src=\"smileys/smile.gif\" alt=\":)\" />." in html)

    def test_tag(self):
        t = Template("""
        {% load smiley_tags %}
        {% smileys %}
        Coding is fun :).
        {% endsmileys %}
        """)
        html = t.render(Context())        
        self.assertTrue("Coding is fun <img class=\"smiley\" src=\"smileys/smile.gif\" alt=\":)\" />." in html)
        
    def test_tag_var(self):
        t = Template("""
        {% load smiley_tags %}
        {% smileys %}
        {{ content }}
        {% endsmileys %}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))        
        self.assertTrue("Coding is fun <img class=\"smiley\" src=\"smileys/smile.gif\" alt=\":)\" />." in html)
