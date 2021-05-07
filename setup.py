from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

DESC = 'A Multi-Level Python Argparse Example'

try:
    README = open(os.path.join(here, 'README.md')).read()
except:
    README = DESC

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    "Programming Language :: Python :: 3.8.5",
]

setup(
    name='multi-level-python-argparse',
    version='1.0.0',
    description=DESC,
    classifiers=CLASSIFIERS,
    author='Ryan Chapin',
    author_email='rchapin@nbinteractive.com',
    long_description=README,
    url='https://github.com/rchapin/multi-level-python-argparse',
    python_requires='>=3.8.5',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
         'console_scripts': [
             'multilevelargparse=multilevelargparse.main:main',
             ],
    },
)
