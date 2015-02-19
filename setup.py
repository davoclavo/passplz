from setuptools import setup

setup(name='passplz',
      version='0.1.1',
      description='A simple password generator',
      url='http://github.com/davoclavo/passplz',
      author='David Gomez Urquiza',
      author_email='d@davo.io',
      license='MIT',
      
      packages=['passplz'],

      test_suite='nose.collector',
      tests_require=['nose', 'nose-cov'],

      scripts=['bin/passplz'],
      )
