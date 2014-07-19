==========================
django-emoticons |mrgreen|
==========================

|travis-develop| |coverage-develop|

Django-emoticons is a django application providing utilities to add
*emoticons* in your templates. Pretty incredible no?

.. contents::

Install
=======

Once you have installed the package in your *PYTHON_PATH*, register the
**emoticons** and **django.contrib.staticfiles** apps in your
*INSTALLED_APPS* project's section. ::

  INSTALLED_APPS = (
    ...
    'django.contrib.staticfiles',
    'emoticons',
    ...
  )

Usage
=====

Filter Usage
------------

For our example we will make a template who display the field *content* of
a model, this field has this value: ::

  Coding is fun and sexy :D

So in our templates we will load the **emoticons_tags** library and use the
**emoticons** filter: ::

  {% load emoticons_tags %}

  {{ object.content|emoticons }}

Which will render:

  Coding is fun and sexy |smile|

Tag Usage
---------

The emoticons app also provides a tag named **emoticons** for converting raw
text. ::

  {% load emoticons_tags %}
  {% emoticons %}
  Documenting is boring but usefull :p
  {% endemoticons %}

Which will render :

  Documenting is boring but usefull |razz|

Index
-----

If you want to retrieve a list of all availables emoticons you can use the
**emoticons_index** tag. ::

  {% load emoticons_tags %}
  {% emoticons_index as emoticons_list %}
  {% for emoticons in emoticons_list %}
  <p>{{ emoticons.0|emoticons }}: {{ emoticons|join:" " }}</p>
  {% endfor %}

Settings
========

You can use differents settings for customizing the application:

* EMOTICONS_DIRECTORY

  The directory where the emoticons files are located, use ``'emoticons'``
  as default.

* EMOTICONS_LIST

  The list of the emoticons used by the application, something like this: ::

    (('(devil)', 'devil.gif'),
     ('(angel)', 'angel.gif'),
     ((':)', ':-)', ':=)', '(smile)'), 'smile.gif'),
     ((':(', ':-(', ':=(', '(sad)'), 'sadsmile.gif'),
    )

If the HTML code of the emoticons does not fit to your needs, you can
override the ``'emoticons/emoticon.html'`` template to adjust it.

.. |razz| image:: http://fantomas.willbreak.it/static/emoticons/tongueout.gif
.. |smile| image:: http://fantomas.willbreak.it/static/emoticons/bigsmile.gif
.. |mrgreen| image:: http://fantomas.willbreak.it/static/emoticons/cool.gif
.. |travis-develop| image:: https://travis-ci.org/Fantomas42/django-emoticons.png?branch=develop
   :alt: Build Status - develop branch
   :target: http://travis-ci.org/Fantomas42/django-emoticons
.. |coverage-develop| image:: https://coveralls.io/repos/Fantomas42/django-emoticons/badge.png?branch=develop
   :alt: Coverage of the code
   :target: https://coveralls.io/r/Fantomas42/django-emoticons
