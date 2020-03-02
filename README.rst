========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/multivar_hypergeom/badge/?style=flat
    :target: https://readthedocs.org/projects/multivar_hypergeom
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/smorin8674/multivar_hypergeom.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/smorin8674/multivar_hypergeom

.. |requires| image:: https://requires.io/github/smorin8674/multivar_hypergeom/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/smorin8674/multivar_hypergeom/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/smorin8674/multivar_hypergeom/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/smorin8674/multivar_hypergeom

.. |version| image:: https://img.shields.io/pypi/v/multivar_hypergeom.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/multivar_hypergeom

.. |wheel| image:: https://img.shields.io/pypi/wheel/multivar_hypergeom.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/multivar_hypergeom

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/multivar_hypergeom.svg
    :alt: Supported versions
    :target: https://pypi.org/project/multivar_hypergeom

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/multivar_hypergeom.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/multivar_hypergeom

.. |commits-since| image:: https://img.shields.io/github/commits-since/smorin8674/multivar_hypergeom/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/smorin8674/multivar_hypergeom/compare/v0.0.0...master



.. end-badges

A Python module for sampling from the Multivariate Hypergeometric distribution.

* Free software: MIT license

Installation
============

::

    pip install multivar_hypergeom

You can also install the in-development version with::

    pip install https://github.com/smorin8674/multivar_hypergeom/archive/master.zip


Documentation
=============


https://multivar_hypergeom.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
