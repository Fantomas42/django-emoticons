"""Urls for the emoticons demo"""
from django.conf.urls import url
from django.conf.urls import patterns
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(
        template_name='demo.html')),
    )
