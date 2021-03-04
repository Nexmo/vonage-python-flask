"""
Flask-Vonage
-------------

This set up a Vonage API client and makes it available to a Flask application
"""
from setuptools import setup


setup(
    name='Flask-Vonage',
    version='0.1',
    url='https://developer.nexmo.com',
    license='MIT',
    author='Chris Tankersley',
    author_email='chris.tankersley@vonage.com',
    description='Bootstrap library for the Vonage Client in Flask',
    long_description=__doc__,
    py_modules=['flask_vonage'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'vonage'
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