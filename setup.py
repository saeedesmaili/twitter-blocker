#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Saeed Esmaili",
    author_email='me@saeedesmaili.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A python package to block fake and toxic twitter accounts in an automated and easy way.",
    entry_points={
        'console_scripts': [
            'twitter_blocker=twitter_blocker.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='twitter_blocker',
    name='twitter_blocker',
    packages=find_packages(include=['twitter_blocker', 'twitter_blocker.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/saeedesmaili/twitter_blocker',
    version='0.0.1',
    zip_safe=False,
)
