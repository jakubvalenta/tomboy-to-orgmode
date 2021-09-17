from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tomboy-to-orgmode',
    version='1.1.0',
    description='Convert Tomboy notes to an Emacs org-mode file.',
    long_description=long_description,
    url='https://github.com/jakubvalenta/tomboy-to-orgmode',
    author='Jakub Valenta',
    author_email='jakub@jakubvalenta.cz',
    license='Apache Software License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'lxml',
        'pytz',
    ],
    entry_points={
        'console_scripts': [
            'tomboy-to-orgmode=tomboy_to_orgmode.tomboy_to_orgmode:main',
        ],
    },
)
