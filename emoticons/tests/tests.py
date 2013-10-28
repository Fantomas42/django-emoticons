"""Tests for emoticons app"""
from django.test import TestCase
from django.template import Context
from django.template import Template


class SmileysTestCase(TestCase):

    def test_filter(self):
        t = Template("""
        {% load emoticon_tags %}
        {{ content|emoticons }}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEquals(html.strip(),
                          'Coding is fun <img class=\"emoticon\" '
                          'src=\"emoticons/smile.gif\" alt=\":)\" />.')

    def test_tag(self):
        t = Template("""
        {% load emoticon_tags %}
        {% emoticons %}
        Coding is fun :).
        {% endemoticons %}
        """)
        html = t.render(Context())
        self.assertEquals(html.strip(),
                          'Coding is fun <img class=\"emoticon\" '
                          'src=\"emoticons/smile.gif\" alt=\":)\" />.')

    def test_tag_var(self):
        t = Template("""
        {% load emoticon_tags %}
        {% emoticons %}
        {{ content }}
        {% endemoticons %}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEquals(html.strip(),
                          'Coding is fun <img class=\"emoticon\" '
                          'src=\"emoticons/smile.gif\" alt=\":)\" />.')

    def test_multiple(self):
        t = Template("""
        {% load emoticon_tags %}
        {% emoticons %}
        {{ content }} :)
        {% endemoticons %}
        """)
        html = t.render(Context({'content': ':) :p'}))
        self.assertEquals(html.strip(), '<img class="emoticon" '
                          'src="emoticons/smile.gif" alt=":)" /> '
                          '<img class="emoticon" src="emoticons/razz.gif" '
                          'alt=":p" /> <img class="emoticon" '
                          'src="emoticons/smile.gif" alt=":)" />')
