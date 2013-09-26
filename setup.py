"""
Flask-RESTAPI
-------------

REST API helpers for Flask projects.
"""

from setuptools import setup

setup(
    name='Flask-RESTAPI',
    version='0.1',
    url='http://github.com/saml/re-stapi/',
    license='BSD',
    author='saml',
    description='REST API helpers for Flask.',
    long_description=__doc__,
    packages=['flask_restapi'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
