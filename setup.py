""" lambdata - Data Science Helper Functions
"""

import setuptools

REQUIRED = [
    'numpy',
    'pandas'
]

with open("README.md",'r') as fh:
     LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name = 'lambdatabbvv33',
    version = '0.0.0.0.1',
    author = 'danh',
    description = 'DS Helper Functions',
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    url='https://github.com/biovir3/lambdata',
    packages = setuptools.find_packages(),
    python_requires = '>=3.5',
    install_requires = REQUIRED,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
