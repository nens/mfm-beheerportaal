from setuptools import setup

version = '0.1.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'gunicorn',
    'raven',  # for sentry logging
    'psycopg2',  # the postgres backend
    'python-memcached',  # for the django memcached backend
    'celery',
    'django-celery-results',  # for handling celery tasks on the web server
    
    ]

tests_require = [
    'nose',
    'coverage',
    'mock',
    ]

setup(name='mfm-beheerportaal',
      version=version,
      description="Multiflexmeter beheerportaal",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='Evert Wielsma, Tim van Osch',
      author_email='timvosch@pollex.nl',
      url='',
      license='proprietary',
      packages=['mfm_beheerportaal'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
