"""Setup script for django-emoticons"""
import os

from setuptools import setup
from setuptools import find_packages

import emoticons

setup(
    name='django-emoticons',
    version=emoticons.__version__,

    description=('A usefull and incredible Django application '
                 'that allow you to use smileys in your templates :)'),
    long_description=open(os.path.join('README.rst')).read(),
    keywords='django, emoticons, smiley',

    author=emoticons.__author__,
    author_email=emoticons.__email__,
    url=emoticons.__url__,

    license=emoticons.__license__,

    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)
