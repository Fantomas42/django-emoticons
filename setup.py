from distutils.core import setup
import os

version = '0.1'

setup(name='django-smileys',
      version=version,

      description=('A usefull and incredible Django application '
                   'that allow you to use smileys in your templates :)'),
      long_description=open(os.path.join('README.rst')).read(),
      keywords='django, smiley',

      author='Fantomas42',
      author_email='fantomas42@gmail.com',
      url='http://github.com/Fantomas42/django-smileys',
      license='BSD License',

      packages=['smileys', 'smileys.templatetags'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules'],
      )
