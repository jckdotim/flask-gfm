"""
Flask-GFM
-------------

GitHub Flavored Markdown jinja2 extension for Flask
"""
from setuptools import setup


__version__ = '0.1.1'

setup(
    name='Flask-GFM',
    version=__version__,
    url='https://github.com/jckdotim/flask-gfm/',
    license='MIT',
    author='JC Kim',
    author_email='jckdotim@gmail.com',
    description='GitHub Flavored Markdown jinja2 extension for Flask',
    long_description=__doc__,
    py_modules=['flask_gfm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'markdown<3.4',
        'py-gfm',
        'Flask-Markdown',
        'python-semantic-release',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup',
    ]
)
