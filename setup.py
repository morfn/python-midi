#!/usr/bin/env python

import os
from setuptools import setup, Extension
import setuptools.command.install

__base__ = {
    'name':'midi', 
    'version':'v0.2.3',
    'description':'Python MIDI API',
    'author':'giles hall',
    'author_email':'ghall@csh.rit.edu',
    'package_dir':{'midi':'src'},
    'py_modules':['midi.containers', 'midi.__init__', 'midi.events', 'midi.util', 'midi.fileio', 'midi.constants'],
    'ext_modules':[],
    'ext_package':'',
    'scripts':[],
}

# this kludge ensures we run the build_ext first before anything else
# otherwise, we will be missing generated files during the copy
class Install_Command_build_ext_first(setuptools.command.install.install):
    def run(self):
        self.run_command("build_ext")
        return setuptools.command.install.install.run(self)

def configure_platform():
    from sys import platform
    ns = __base__.copy()
    return ns

if __name__ == "__main__":
    setup(**configure_platform())


