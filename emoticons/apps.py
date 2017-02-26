"""Apps for emoticons"""
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class EmoticonConfig(AppConfig):
    """
    Config for Emoticons application.
    """
    name = 'emoticons'
    label = 'emoticons'
    verbose_name = _('Emoticons')
