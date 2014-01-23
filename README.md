buildlist
=========

Tool to display ordered list of builds to launch in order to make a package, based on dependencies between packages

Dependencies are described with a file in YAML format, see [sample.yml](https://github.com/sebbrochet/buildlist/blob/master/sample.yml) file.

And ordered list of build for a specific package can be requested as follow:
```
# buildlist -g sample.yml -p package1
package4,package3,package2,package1
```

Requirements:
------------
* Python 2.x
* pyyaml library

Installation:
-------------
* pip install -r requirements.txt
* python setup.py install

usage
-----

```
usage: buildlist [-h] [-g GRAPH] [-p PACKAGE] [--v]

Display dependencies for a package.

optional arguments:
  -h, --help            show this help message and exit
  -g GRAPH, --graph GRAPH
                        Graph file to use
  -p PACKAGE, --package PACKAGE
                        Package to look for
  --v                   Print program version and exit.
```

