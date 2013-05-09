import os
from setuptools import setup, find_packages
import localized_names as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="django-localized-names",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app, names, localization, l10n',
    author='Daniel Kaufhold',
    author_email='daniel.kaufhold@bitmazk.com',
    url="https://github.com/bitmazk/django-localized-names",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.4.3',
        'South',
        'django-libs',
    ],
    tests_require=[
        'fabric',
        'factory_boy<2.0.0',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
    ],
    test_suite='localized_names.tests.runtests.runtests',
)
