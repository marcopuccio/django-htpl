# -*- coding:utf8 -*-

# Distributed under the MIT license, see LICENSE

from setuptools import setup, find_packages
import sys, os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='htpl', 
      version=0.1, 
      description="Simple app made of django generic views for using the\
              template features during frontend development process",
      packages=find_packages()find_packages(),
      include_package_data=True,
      install_requires=[
          'django>=1.9',
      ],
      zip_safe=False,
      author='mars0n',
      url='http://github.com/mars0n/django-htpl',
      classifiers = [
          'Enviroment :: Web Enviroment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: MIT Licence',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
      ],
)

