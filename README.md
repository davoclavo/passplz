Deploy your Python Package 101
==============================

Example package
---------------

```tree
passplz
├── bin
│   └── passplz
├── passplz
│   ├── __init__.py
│   └── tests
│       └── __init__.py
├── setup.cfg
└── setup.py
```


`setup.py` file
---------------

  * [It is a setup script](https://docs.python.org/2/distutils/setupscript.html)
    - *Is the centre of all activity in building, distributing, and installing modules using the Distutils*
  * Used to install a package doing
    - `python setup.py install`
    - `pip install .`
  * Also used to deploy your package to PyPI

*Example*

```py
from setuptools import setup

setup(name='passplz',
      version='0.1.0',
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
```


`requirements.txt` file
-----------------------

  * pip-only
  * List of requirements or dependencies
  * Useful for "private applications", such as a webapp that won't be pushed to PyPI
  * I use it for development dependencies (such as test dependencies), but would be way cooler to have it all in `setup.py` and `setup.cfg



Deploying to PyPI
-----------------

  1. Create a PyPI account
  2. Register your package:
    - `python setup.py register -r pypitest`
    - `python setup.py register -r pypi`
  3. Upload your package:
    - `python setup.py sdist upload -r pypitest`
    - `python setup.py sdist upload -r pypi`
  4. Remember to bump versions if a new version is deployed


Tests
-----

  * `python setup.py test`
  * This is a bomb if you are using `nose` because you can load plugins
    - `python setup.py nosetests`


`setup.cfg` file
----------------
  * setup.py's sidekick

  ```
  [nosetests]
  with-coverage=1
  cover-package=passplz
  ```

Continuous Integration using [Travis CI](https://travis-ci.com)
----------------------------------------

  * Signin using Github
  * Flick the switch on your project at [travis-ci.org/profile](https://travis-ci.org/profile)
  * Add a `.travis.yml` file to your repo
  * Push changes to github
  * [PyPI deployment](http://docs.travis-ci.com/user/deployment/pypi/)
    - Add deploy key to your .yml
    - Encrypt your PyPI password: `travis encrypt --add deploy.password`

Example:

```yml
language: python
sudo: false
python:
  - '2.6'
  - '2.7'
  - '3.3'
  - '3.4'
  - pypy
deploy:
  provider: pypi
  user: davoclavo
  password:
    secure: ib4iaqycgcF3ijSC...
install:
  - pip install .
  - pip install -r dev-requirements.txt
  - pip install coveralls
script: 
  - PYTHONPATH=. nose2 -v --with-cov
after_success: coveralls
```


Coverage using [coveralls.io](https://coveralls.io/)
----------------------------

  * Signup using Github
  * Add to your `.travis.yml`:

    ```
    script:
      - ... --with-cov
    install:
      ...
      - pip install coveralls
    after_success:
      - coveralls
    ```


README.md
---------

  * Add install instructions

~~~md

    Installation
    ============

    From pip

    ```
    pip install passplz
    ```

    From source

    ```
    git clone https://github.com/davoclavo/passplz.git
    cd passplz
    python setup.py install
    pip install -r dev-requirements.txt
    ```

~~~

  * Add badges (shields) using [shields.io](http://shields.io/)
    - [![](https://travis-ci.org/davoclavo/passplz.svg?branch=master)](https://travis-ci.org/davoclavo/passplz)
    - [![](https://img.shields.io/coveralls/davoclavo/passplz.svg)](https://coveralls.io/r/davoclavo/passplz)
    - [![](https://img.shields.io/pypi/v/passplz.svg)](https://pypi.python.org/pypi/passplz)
    - [![](https://img.shields.io/badge/coolness-ultrasupercool-blue.svg)](http://i.imgur.com/oJ6ZZf8.gif)

~~~
[![](https://travis-ci.org/davoclavo/passplz.svg?branch=master)](https://travis-ci.org/davoclavo/passplz)
[![](https://img.shields.io/coveralls/davoclavo/passplz.svg)](https://coveralls.io/r/davoclavo/passplz)
[![](https://img.shields.io/pypi/v/passplz.svg)](https://pypi.python.org/pypi/passplz)
[![](https://img.shields.io/badge/coolness-ultrasupercool-blue.svg)](http://i.imgur.com/oJ6ZZf8.gif)
~~~



Useful references
-----------------

  * [How To Package Your Python Code](http://www.scotttorborg.com/python-packaging/index.html)
  * [Python Packaging User Guide](https://packaging.python.org/en/latest/)
