==========================
django-emoticons |mrgreen|
==========================

|travis-develop| |coverage-develop|

Django-emoticons is a django application providing utilities to add
*emoticons* in your templates.

.. contents::

Install
=======

Install the package in your *PYTHON_PATH* by getting the sources and run
**setup.py** or use *pip*::

  $ pip install -e git://github.com/Fantomas42/django-emoticons.git#egg=django-emoticons

Then register the **emoticons** app in your *INSTALLED_APPS* project's
section.

Examples
========

Filter Usage
------------

For our example we will make a template who display the field *content* of
a model, this field has this value: ::

  Coding is fun and sexy :D

So in our templates we will load the **emoticon_tags** library and use the
**emoticons** filter: ::

  {% load emoticon_tags %}

  {{ object.content|emoticons }}

Which will render:

  Coding is fun and sexy |smile|

Tag Usage
---------

The emoticons app also provides a tag named **emoticons** for converting raw
text. ::

  {% load emoticon_tags %}
  {% emoticons %}
  Documenting is boring but usefull :p
  {% endemoticons %}

Which will render :

  Documenting is boring but usefull |razz|

So cool, no ?

Settings
========

You can use differents settings for customizing the application:

* EMOTICONS_URL

  The url where the emoticons files are located, use this as default.::

    os.path.join(settings.MEDIA_URL, 'emoticons/'))

* EMOTICONS_CLASS

  The class wo will be applied to the *img* markup of the emoticons.

* EMOTICONS_LIST

  The list of the emoticons who will be converted. It's something like that: ::

    ((':)', 'smile.gif'),
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

Of course the package does not provide the images, is your job to find and
set them in your project.

.. |razz| image:: http://static.fache.fr/img/smileys/razz.gif
.. |smile| image:: http://static.fache.fr/img/smileys/smile.gif
.. |mrgreen| image:: http://static.fache.fr/img/smileys/mrgreen.gif
.. |travis-develop| image:: https://travis-ci.org/Fantomas42/django-emoticons.png?branch=develop
   :alt: Build Status - develop branch
   :target: http://travis-ci.org/Fantomas42/django-emoticons
.. |coverage-develop| image:: https://coveralls.io/repos/Fantomas42/django-emoticons/badge.png?branch=develop
   :alt: Coverage of the code
   :target: https://coveralls.io/r/Fantomas42/django-emoticons
