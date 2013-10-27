"""Settings for emoticons app"""
from os.path import join
from django.conf import settings

emoticons_default_list = ((':)', 'smile.gif'),
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

EMOTICONS_URL = getattr(settings, 'EMOTICONS_URL',
                        join(settings.MEDIA_URL, 'emoticons/'))
EMOTICONS_LIST = getattr(settings, 'EMOTICONS_LIST', emoticons_default_list)
EMOTICONS_CLASS = getattr(settings, 'EMOTICONS_CLASS', 'emoticon')
