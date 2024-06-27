from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='seaweed',

    version='1.0.0',

    description='A package for generating and exporting moments of the target state distribution after an ownship manoeuvre',

    long_description=long_description,

    long_description_content_type='text/markdown',

    author='Athena Xiourouppa',

    author_email='athena.xiourouppa@acaciasystems.com.au',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3',
    ],

    install_requires=[
        'numpy',
        'pytest',
        'qmcpy',
        'yapf',
        'sage',
    ],

    packages=find_packages(where='seaweed'),

    python_requires='>=3.10',
)
