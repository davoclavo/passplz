from setuptools import setup

setup(name='passplz',
      version='1.33.78',
      description='A simple password generator',
      url='http://github.com/davoclavo/passplz',
      author='David Gomez Urquiza',
      author_email='d@davo.io',
      license='MIT',

      packages=['passplz'],

      test_suite='nose.collector',
      tests_require=['nose', 'nose-cov'],

      scripts=['bin/passplz'],

      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Topic :: Security',
                   'Topic :: Utilities'],
      )
