# coding=utf-8
from setuptools import setup

setup(
    name='bar-chooser',
    version='0.1.0',
    packages=['bar_chooser'],
    url='https://github.com/strizhechenko/bar-chooser',
    license='MIT',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    description='Script that help you to choose a bar to drink with someone.',
    entry_points={
        'console_scripts': [
            'bar-chooser=bar_chooser.__init__:main',
        ],
    },
)
