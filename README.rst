django-smileys
==============

Django-smileys is a django application providing a method to put *smiley images* in your content
by simply adding a **tag_filter** in yours templates. |smiley|

.. contents::

Install
-------

::

  $> easy_install django-smileys

Then register the **smileys** app in your *INSTALLED_APPS* project's section.


Example
-------

For our example we will make a template who display the field **content** of our model with smileys integrated.

This field has this value ::

  Coding is fun and sexy :D

So in our templates we will load the smiley_tags library and use the **smileys** filter

  {% load smiley_tags %}
      
  {{ object.content|smileys }}

Wich will render :

  Coding is fun and sexy |big_smiley|

Easy, no ?

Of course you can use this filter anywhere you want in your template.

Settings
--------

You can use differents settings for customizing the application.

* SMILEYS_URL

The url where the smileys files are located, use this as default ::

    os.path.join(settings.MEDIA_URL, 'smileys/'))

* SMILEYS_CLASS

The class wo will be applied to the *img* markup of the smileys.

* SMILEYS_LIST

The list of the smileys who will be converted. It's something like that ::

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

Of course the package does not provide the smileys files, 
is your job to find and set them in your project.

.. |smiley| image:: http://fantomas.willbreak.it//img/smileys/mrgreen.gif
.. |big_smiley| image:: http://fantomas.willbreak.it//img/smileys/smile.gif

