#/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys


# if sys.version_info[:3] < (3, 4):
#     raise SystemExit("Toga requires Python 3.4+.")
#
#
# with io.open('toga/__init__.py', encoding='utf8') as version_file:
#     version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
#     if version_match:
#         version = version_match.group(1)
#     else:
#         raise RuntimeError("Unable to find version string.")
#
#
# with io.open('README.rst', encoding='utf8') as readme:
#     long_description = readme.read()


setup(
    name='toga',
    version=0.1,
    description='A Python native, OS native GUI toolkit.',
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://pybee.org/toga',
    packages=find_packages(exclude='tests'),
    install_requires=[
        'colosseum>=0.1.6'
    ],
    license='New BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Widget Sets',
    ],
    zip_safe=False,
)
