# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os.path import join

version = '2.0'
readme = open(join('src', 'dolmen', 'widget', 'tinymce', 'README.txt')).read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'fanstatic',
    'dolmen.template',
    'js.jquery',
    'js.tinymce',
    'setuptools',
    'dolmen.forms.base',
    'dolmen.forms.ztk',
    'zope.interface',
    ],

tests_require = [
    'grokcore.component',
    'dolmen.forms.ztk [test]',
    'cromlech.browser [test] >= 0.5',
    'zope.component',
    'zope.interface',
    'zope.schema',
    'zope.security',
    'zope.i18n',
    ]

setup(name='dolmen.widget.tinymce',
      version=version,
      description="A rich text widget using TinyMCE for Cromlech",
      long_description=readme + '\n\n' + history,
      keywords='Cromlech Widget TinyMCE Dolmen',
      author='Souheil Chelfouh',
      author_email='trollfot@gmail.com',
      url='http://gitweb.dolmen-project.org/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['dolmen', 'dolmen.widget'],
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      extras_require={'test': tests_require},
      classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
      ],
      entry_points="""
      [fanstatic.libraries]
      jquerytinymce = dolmen.widget.tinymce:DolmenTinyLibrary
      """,
      )
