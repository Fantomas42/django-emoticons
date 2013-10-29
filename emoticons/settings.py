"""Settings for emoticons app"""
import re

from os.path import join
from django.conf import settings

emoticons_default_list = (
    (':)', 'smile.gif'),
    (':D', 'mrgreen.gif'),
    (':(', 'sad.gif'),
    (':|', 'neutral.gif'),
    (';)', 'wink.gif'),
    (':p', 'razz.gif'),
    (':P', 'razz.gif'),
    (':o', 'surprised.gif'),
    (':O', 'surprised.gif'),
    (':s', 'confused.gif'),
    (':S', 'confused.gif'),
    (':$', 'confused.gif'),
    ('o_O', 'eek.gif'),
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

EMOTICONS_URL = getattr(settings, 'EMOTICONS_URL',
                        join(settings.MEDIA_URL, 'emoticons/'))

EMOTICONS_CLASS = getattr(settings, 'EMOTICONS_CLASS', 'emoticon')
