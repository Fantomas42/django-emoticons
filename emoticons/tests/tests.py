"""Tests for emoticons app"""
from django.test import TestCase
from django.template import Context
from django.template import Template
from django.template import TemplateSyntaxError

from emoticons.templatetags.emoticons_tags import emoticons_index


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
        {% load emoticons_tags %}
        {{ content|emoticons }}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEmoticons(html)

    def test_filter_exclude(self):
        t = Template("""
        {% load emoticons_tags %}
        {{ content|safe|emoticons:'a,b' }}
        """)
        html = t.render(Context({
            'content': ('<p>Coding is fun :).</p>'
                        '<b>Coding is fun :).</b>'
                        '<a>Coding is fun :).</a>')}))
        self.assertEmoticons(
            html,
            '<p>Coding is fun <img alt=":)" '
            'class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif"/>.</p>'
            '<b>Coding is fun :).</b>'
            '<a>Coding is fun :).</a>')

    def test_tag(self):
        t = Template("""
        {% load emoticons_tags %}
        {% emoticons %}
        Coding is fun :).
        {% endemoticons %}
        """)
        html = t.render(Context())
        self.assertEmoticons(html)

    def test_tag_invalid(self):
        with self.assertRaises(TemplateSyntaxError):
            Template("""
            {% load emoticons_tags %}
            {% emoticons to much args %}
            Coding is fun :).
            {% endemoticons %}
            """)

    def test_tag_exclude(self):
        t = Template("""
        {% load emoticons_tags %}
        {% emoticons 'b' %}
        <p>Coding is fun :).</p>
        <b>Coding is fun :).</b>
        <a>Coding is fun :).</a>
        {% endemoticons %}
        """)
        html = t.render(Context())
        self.assertEmoticons(
            html,
            '<p>Coding is fun <img alt=":)" '
            'class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif"/>.</p>\n'
            '<b>Coding is fun :).</b>\n'
            '<a>Coding is fun <img alt=":)" '
            'class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif"/>.</a>')
        t = Template("""
        {% load emoticons_tags %}
        {% emoticons 'a,b' %}
        <p>Coding is fun :).</p>
        <b>Coding is fun :).</b>
        <a>Coding is fun :).</a>
        {% endemoticons %}
        """)
        html = t.render(Context())
        self.assertEmoticons(
            html,
            '<p>Coding is fun <img alt=":)" '
            'class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif"/>.</p>\n'
            '<b>Coding is fun :).</b>\n'
            '<a>Coding is fun :).</a>')

    def test_tag_exclude_var(self):
        t = Template("""
        {% load emoticons_tags %}
        {% emoticons exclude %}
        <p>Coding is fun :).</p>
        <b>Coding is fun :).</b>
        <a>Coding is fun :).</a>
        {% endemoticons %}
        """)
        html = t.render(Context({'exclude': 'p,a'}))
        self.assertEmoticons(
            html,
            '<p>Coding is fun :).</p>\n'
            '<b>Coding is fun <img alt=":)" '
            'class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif"/>.</b>\n'
            '<a>Coding is fun :).</a>')

    def test_tag_exclude_with_inner_html(self):
        expected_html = ('<p>Fini l\'epoque du <em>Ctrl+F5</em> toutes '
                         'les 15 secondes. <img alt=":)" class="emoticon '
                         'emoticon-3a29" src="/emoticons/smile.gif"/></p>')
        t = Template("""
        {% load emoticons_tags %}
        {% emoticons "b" %}
        <p>Fini l'epoque du <em>Ctrl+F5</em> toutes les 15 secondes. :)</p>
        {% endemoticons %}
        """)
        self.assertEmoticons(t.render(Context()), expected_html)

        t = Template("""
        {% load emoticons_tags %}
        {{ content|safe|emoticons:"b" }}
        """)
        self.assertEmoticons(t.render(
            Context({'content': (
                "<p>Fini l'epoque du <em>Ctrl+F5</em> "
                "toutes les 15 secondes. :)</p>")})),
            expected_html)

    def test_tag_var(self):
        t = Template("""
        {% load emoticons_tags %}
        {% emoticons %}
        {{ content }}
        {% endemoticons %}
        """)
        html = t.render(Context({'content': 'Coding is fun :).'}))
        self.assertEmoticons(html)

    def test_multiple(self):
        t = Template("""
        {% load emoticons_tags %}
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
            'src="/emoticons/tongueout.gif" alt=":p" /> '
            '<img class="emoticon emoticon-3a29" '
            'src="/emoticons/smile.gif" alt=":)" />')

    def test_index(self):
        self.assertEquals(len(emoticons_index()), 84)
