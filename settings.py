"""Settings for smileys app"""
from os.path import join
from django.conf import settings

smileys_default_list = ((':)', 'smile.gif'),
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

SMILEYS_URL = getattr(settings, 'SMILEYS_URL',
                      join(settings.MEDIA_URL, 'smileys/'))
SMILEYS_LIST = getattr(settings, 'SMILEYS_LIST', smileys_default_list)
SMILEYS_CLASS = getattr(settings, 'SMILEYS_CLASS', 'smiley')

