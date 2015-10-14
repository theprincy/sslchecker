"""
sslchecker
==========

Check SSL certificates of a site on your command line.

"""
from setuptools import setup


extras_require = {
    'test': [
        'coveralls',
        'pyopenssl',
        'pytest',
        'pytest-cov',
    ]
}

setup(
    name='sslchecker',
    version='0.1.0',
    url='https://github.com/raccoonyy/sslchecker',
    author='Seungho Kim',
    author_email='raccoonyy@gmail.com',
    description='Check SSL certificates of a site on your command line',
    long_description=__doc__,
    packages=['sslchecker'],
    entry_points={
        'console_scripts': ['sslchecker = sslchecker.cli:cli']
    },
    extras_require=extras_require,
    install_requires=[
        'click',
        'colorama',
        'netlib',
        'pycountry',
        'pyopenssl',
    ],
    tests_require=extras_require['test'],
    test_suite="py.test",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)