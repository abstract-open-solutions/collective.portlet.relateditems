import os
from setuptools import setup, find_packages

version = '0.3.1'

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('CHANGES.txt')
)

setup(name='collective.portlet.relateditems',
      version=version,
      description="A Plone portlet to display similar items to context",
      long_description=long_description,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='related, categories, keywords',
      author='Rui Guerra <rui@v2.nl>, kiorky <kiorky@cryptelium.net>',
      #author_email='rui AT v2 DOT nl',
      #url='https://svn.v2.nl/plone/collective.portlet.relateditems/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )