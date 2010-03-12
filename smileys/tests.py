"""Tests for smileys app"""
from django.test import TestCase
from django.template import Context, Template

class SmileysTestCase(TestCase):

    def test_filter(self):
        t = Template("""
        {% load smiley_tags %}
        {{ content|smileys }}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEquals(html.strip(), 'Coding is fun <img class=\"smiley\" src=\"smileys/smile.gif\" alt=\":)\" />.')

    def test_tag(self):
        t = Template("""
        {% load smiley_tags %}
        {% smileys %}
        Coding is fun :).
        {% endsmileys %}
        """)
        html = t.render(Context())
        self.assertEquals(html.strip(), 'Coding is fun <img class=\"smiley\" src=\"smileys/smile.gif\" alt=\":)\" />.')

    def test_tag_var(self):
        t = Template("""
        {% load smiley_tags %}
        {% smileys %}
        {{ content }}
        {% endsmileys %}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEquals(html.strip(), 'Coding is fun <img class=\"smiley\" src=\"smileys/smile.gif\" alt=\":)\" />.')


    def test_multiple(self):
        t = Template("""
        {% load smiley_tags %}
        {% smileys %}
        {{ content }} :)
        {% endsmileys %}
        """)
        html = t.render(Context({'content': ':) :p'}))
        self.assertEquals(html.strip(), '<img class="smiley" src="smileys/smile.gif" alt=":)" /> '\
                          '<img class="smiley" src="smileys/razz.gif" alt=":p" /> '\
                          '<img class="smiley" src="smileys/smile.gif" alt=":)" />')


