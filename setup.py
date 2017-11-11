# coding=utf-8
import os
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='bar-chooser',
    version='0.1.3',
    packages=['bar_chooser'],
    url='https://github.com/strizhechenko/bar-chooser',
    license='MIT',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    description='Script that help you to choose a bar to drink with someone.',
    long_description=(read('README.rst')),
    entry_points={
        'console_scripts': [
            'bar-chooser=bar_chooser.__init__:main',
        ],
    },
)
