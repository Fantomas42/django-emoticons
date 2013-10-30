"""Tests for emoticons app"""
from django.test import TestCase
from django.template import Context
from django.template import Template


class EmoticonsTestCase(TestCase):
    expected_result = (
        'Coding is fun <img class="emoticon emoticon-3a29" '
        'src="/emoticons/smile.gif" alt=":)" />.'
    )

    def assertEmoticons(self, html1, html2=None):
        if html2 is None:
            html2 = self.expected_result
        html1 = html1.strip()
        html2 = html2.strip()
        self.assertEquals(html1, html2)

    def test_filter(self):
        t = Template("""
        {% load emoticon_tags %}
        {{ content|emoticons }}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEmoticons(html)

    def test_tag(self):
        t = Template("""
        {% load emoticon_tags %}
        {% emoticons %}
        Coding is fun :).
        {% endemoticons %}
        """)
        html = t.render(Context())
        self.assertEmoticons(html)

    def test_tag_var(self):
        t = Template("""
        {% load emoticon_tags %}
        {% emoticons %}
        {{ content }}
        {% endemoticons %}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEmoticons(html)

    def test_multiple(self):
        t = Template("""
        {% load emoticon_tags %}
        {% emoticons %}
        {{ content }} :)
        {% endemoticons %}
        """)
        html = t.render(Context({'content': ':) :p'}))
        self.assertEmoticons(
            html,
            '<img class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif" alt=":)" /> '
            '<img class="emoticon emoticon-3a70" '
            'src="/emoticons/razz.gif" alt=":p" /> '
            '<img class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif" alt=":)" />')
