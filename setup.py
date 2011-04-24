# Setup file for feedstail
from setuptools import setup

# Import from feedstail
from feedstail import __version__


with open('README.rst') as readme:
    long_description = readme.read()

setup( name             = "feedstail"
     , description      = "A tail-f-like utility for feeds"
     , long_description = long_description
     , license          = "GNU General Public License v3"
     , url              = "https://gitorious.org/feedstail/feedstail"

     , author           = "Romain Gauthier"
     , author_email     = "romain.gauthier@masteri2l.org"

     , version          = __version__
     , scripts          = ['bin/feedstail']
     , packages         = ['feedstail']
     , data_files       = [('', ['README.rst', 'LICENSE.txt'])]
     , install_requires = ['argparse', 'FeedParser']

     , classifiers      =
         [ "Development Status :: 3 - Alpha"
         , "License :: OSI Approved :: GNU General Public License (GPL)"
         , "Operating System :: OS Independent"
         , "Programming Language :: Python :: 2.6"
         , "Topic :: Utilities"
         ]
      )

