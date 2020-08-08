# -*- coding: utf-8 -*-
import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    README = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ebay-accounts',
    version='2.2.0',
    zip_safe=False,
    packages=['ebay_accounts', 'ebay_accounts.migrations'],
    include_package_data=True,
    license='BSD License',
    description='A Django app for managing Ebay accounts',
    long_description=README,
    url='https://github.com/luke-dixon/django-ebay-accounts',
    author='Luke Dixon',
    author_email='luke@luke.dixon.name',
    install_requires=[
        'xmltodict',
        'requests',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 fileencoding=utf-8
