Django Localized Names
======================


.. WARNING::
    This is early alpha. Please stand by to await a stable pypi version.

A reusable Django app to provide a correct order for names according to the
currently set language.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django

If you want to install the latest stable release from PyPi::

    $ pip install django-localized-names

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-localized-names.git#egg=localized_names

Add ``localized_names`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'localized_names',
    )

Usage
-----


Model interface
===============

Since this app does not know about your specific model (let's call it
``Person`` in our example), that holds the values for names and title, it
expects that you implement the following methods.
Example::

    class Person(models.Model):
        """Holds the information about a person in your system."""

        # your fields go here

        def get_title(self):
            """Returns either 'Mr.' or 'Mrs.' depending on the gender."""
            return 'Mr.'
        def get_romanized_first_name()
            """Returns the first name in roman letters."""
            return self.first_name  # e.g. Zhang
        def get_romanized_last_name()
            """Returns the first name in roman letters."""
            return self.last_name  # e.g. Mingshun
        def get_non_romanized_first_name()
            """Returns the non roman version of the first name."""
            return self.chinese_first_name  # e.g. 张
        def get_non_romanized_last_name()
            """Returns the non roman version of the first name."""
            return self.chinese_last_name  # e.g. 明顺
        def get_nickname()
            """Returns the nickname of a person in roman letters."""
            return self.nickname  # e.g. Jack


Templatetag
===========

To get the name of a `person`, you just use the templatetag in template like so
`{{ person|get_name "SHORT_NAME_FORMAT" }}`.

Alternatively you can provide `"LONG_NAME_FORMAT"`, which is the default.


Settings
========

The app provides standard settings for German, English and Chinese.

If you want to override our standards, you can set the
`CUSTOM_FORMAT_MODULE_PATHS` setting (it defaults to
[`localized_names.formats`, ]).
If you provide additional formats, you simply extend the setting. ::

    CUSTOM_FORMAT_MODULE_PATHS = [
        'localized_names.formats',
        'my_app.formats',
    ]


Add or override formats
=======================

This app makes use of Django's existing locale formats framework.
So you will want to use the following folder structure for adding new formats:

::

    my_app/
        formats/
            __init__.py
            en/
                __init__.py
                formats.py

This is further described here:

https://docs.djangoproject.com/en/dev/topics/i18n/formatting/#creating-custom-format-files

The `formats.py` will then need a setting for `SHORT_NAME_FORMAT` and
`LONG_NAME_FORMAT`.

Possible options are ::

    t = title
    t = title capitalized
    f = romanized first name
    F = romanized first name capitalized
    l = romanized last name
    L = romanized last name capitalized
    a  = non romanized first name
    A = non romanized name capitalized
    x  = non romanized last name
    X = non romanized last name capitalized
    n = nickname
    N = nickname capitalized

For example ::

    LONG_NAME_FORMAT = '{a}{x}{t} ({L}, "{n}", {f})'

would yield in the following formatted name:

    `张明顺先生 (ZHANG, "Jack", Mingshun)`


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-localized-names
    $ pip install -r requirements.txt
    $ ./localized_names/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
