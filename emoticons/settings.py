"""Settings for emoticons app"""
import re

from django.conf import settings

try:
    unicode = unicode
except NameError:  # Python 3
    unicode = str
    basestring = (str, bytes)


emoticons_default_list = (
    (':(', 'sad.gif'),
    (';)', 'wink.gif'),
    ('o_O', 'eek.gif'),
    (':)', 'smile.gif'),
    (':D', 'mrgreen.gif'),
    (':|', 'neutral.gif'),
    ((':p', ':P'), 'razz.gif'),
    ((':s', ':s', ':$'), 'confused.gif'),
    ((':o', ':O', ':0'), 'surprised.gif'),
)


def build_emoticons_regexp(emoticons_list):
    """
    Build a new list of emoticon tuples.
    Each tuple contains a regexp of the emoticon,
    the original name and the image associated.
    """
    emoticons_regexp = []
    for emoticons, image in emoticons_list:
        if isinstance(emoticons, basestring):
            emoticons = [emoticons]
        for emoticon in emoticons:
            emoticons_regexp.append(
                (re.compile(re.escape(emoticon)),
                 emoticon, image))
    return emoticons_regexp


EMOTICONS_LIST = getattr(settings, 'EMOTICONS_LIST',
                         emoticons_default_list)

EMOTICONS_REGEXP = build_emoticons_regexp(EMOTICONS_LIST)

EMOTICONS_DIRECTORY = getattr(settings, 'EMOTICONS_DIRECTORY', 'emoticons')
