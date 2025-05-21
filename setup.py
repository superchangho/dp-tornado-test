# -*- coding: utf-8 -*-
"""
MVC Web Application Framework with Tornado, Python 2 and 3

To install the package run:

    pip install dp-tornado


Run
-----

    $ pip install virtualenv
    $ virtualenv ./venv
    $ . ./venv/bin/activate
    $ pip install dp-tornado
    $ dp4p init --path app

"""


import sys
import os


from setuptools import setup

try:
    from setuptools.command.install import install

except ImportError:
    from distutils.command.install import install


with open('dp_tornado/version.py', 'r') as fp_v:
    for c in fp_v.read().split('\n'):
        exec(c)


dp_project_name = 'dp-tornado'
dp_version = __version__
dp_github_url = 'http://github.com/why2pac/dp-tornado'
dp_license = 'MIT'

dp_author = 'Parker'
dp_author_email = 'oss@dp.farm'

dp_maintainer = dp_author
dp_maintainer_email = dp_author_email

dp_description = 'MVC Web Application Framework with Tornado.'


install_requires = [
        'BeautifulSoup4>=4.7.1',
        'boto3>=1.9.111',
        'croniter>=0.3.30',
        'CyMySQL>=0.9.13',
        'httpagentparser>=1.8.2',
        'lxml>=4.3.2',
        'Pillow>=5.4.1',
        'pycrypto>=2.6.1',
        'pytz>=2018.9',
        'redis>=3.2.0',
        'requests>=2.21.0',
        'SQLAlchemy>=1.3.1',
        'tornado>=4.5.3,<5.0.0',
        'validate_email>=1.3',
        'validators>=0.12.4',
        'wand>=0.5.1',
        # , 'selenium'
    ]


if sys.version_info[0] <= 2:
    install_requires.append('futures==3.0.5')


# Will not install pillow when it starts from readthedocs.
# if os.environ.get('READTHEDOCS') != 'True':
#     pass


setup(
    name=dp_project_name,
    version=dp_version,
    url=dp_github_url,
    license=dp_license,
    author=dp_author,
    author_email=dp_author_email,
    maintainer=dp_maintainer,
    maintainer_email=dp_maintainer_email,
    description=dp_description,
    long_description=__doc__,
    packages=['dp_tornado'],
    include_package_data=True,
    install_requires=install_requires,
    keywords=['MVC', 'Web Application Framework'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    entry_points={
        'console_scripts': [
            'dp4p = dp_tornado.cli:main'
        ]
    }
)
