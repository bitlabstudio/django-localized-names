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
        'Django',
        'django-libs',
    ],
)
