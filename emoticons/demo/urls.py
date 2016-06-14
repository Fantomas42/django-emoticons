"""Urls for the emoticons demo"""
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(
        template_name='demo.html')),
]
