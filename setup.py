from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tomboy-to-orgmode',

    version='1.0.0',

    description='Convert Tomboy notes to an Emacs org-mode file.',
    long_description=long_description,

    url='https://lab.saloun.cz/jakub/tomboy-to-orgmode',

    author='Jakub Valenta',
    author_email='jakub@jakubvalenta.cz',

    license='Apache Software License',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],

    keywords='',

    packages=find_packages(),

    install_requires=[
        'attr',
        'beautifulsoup4',
    ],

    entry_points={
        'console_scripts': [
            'tomboy-to-orgmode=tomboy_to_orgmode.tomboy_to_orgmode:main',
        ],
    },
)
