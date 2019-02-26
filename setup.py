#!/usr/bin/env python

# NOTE: most of the configuration is defined in setup.cfg

import sys
from distutils.version import LooseVersion

import pip
import setuptools
from setuptools import setup

if LooseVersion(pip.__version__) < '18.0':
    sys.stderr.write("ERROR: pip 18.0 or later is required by aas-timeseries\n")
    sys.exit(1)

if LooseVersion(setuptools.__version__) < '30.3':
    sys.stderr.write("ERROR: setuptools 30.3 or later is required by aas-timeseries\n")
    sys.exit(1)

setup(use_scm_version=True,
      setup_requires=['setuptools_scm'])
