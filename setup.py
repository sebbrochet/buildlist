#!/usr/bin/env python

import os
import sys

from distutils.core import setup

__version__ = '0.1.0'
__author__ = '@sebbrochet'

setup(name='buildlist',
      version=__version__,
      description='Tool to display ordered list of builds to launch in order to make a package, based on dependencies between packages',
      long_description='This command-line tool lets you describe in YAML dependencies between packages and request the ordered list of builds to launch to make a specific package.',
      author=__author__,
      author_email='contact@sebbrochet.com',
      platforms=['linux'],
      license='MIT License',
      scripts=[
         'bin/buildlist'
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Software Development :: Build Tools',
          ],
      )
