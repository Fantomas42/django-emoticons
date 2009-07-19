django-smileys
==============

Django-smilyes is a django application providing a method to put *smileys* in your content
by simply adding a **tag_filter** in yours templates.

Examples
--------

For our example we will make a template who display the field *content* of our
model with smileys integrated.

We suppose that you have register the *smileys* app in your *INSTALLED_APPS* section.

   {% load smiley_tags %}

   {{ object.content|smileys }}


Easy, no ?

Of course you can use this filter anywhere you want in your template.

Settings
--------

You can use differents settings for customizing the application.

* SMILEYS_URL

The url where the smileys files are located, use this as default :

    os.path.join(settings.MEDIA_URL, 'smileys/'))

* SMILEYS_CLASS

The class wo will be applied to the *img* markup of the smileys.

* SMILEY_LIST

The list of the smileys who will be converted. It's something like that :

    ((':)', 'smile.gif'),
     (':D', 'mrgreen.gif'),
     (':(', 'sad.gif'),
     (':|', 'neutral.gif'),
     (';)', 'wink.gif'),
     (':p', 'razz.gif'),
     (':P', 'razz.gif'),
     (':o', 'surprised.gif'),
     (':O', 'surprised.gif'),)

Of course the package does not provide the smileys files, 
is your job to find and set them in your project.