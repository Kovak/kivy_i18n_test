# Copyright (C) 2009-2012 by Barry A. Warsaw
#
# This file is part of flufl.i18n
#
# flufl.i18n is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# flufl.i18n is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with flufl.i18n.  If not, see <http://www.gnu.org/licenses/>.

"""Test harness for doctests."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'additional_tests',
    ]


import os
import atexit
import doctest
import unittest

from pkg_resources import (
    resource_filename, resource_exists, resource_listdir, cleanup_resources)


DOCTEST_FLAGS = (
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE |
    doctest.REPORT_NDIFF)


def setup(testobj):
    """Test setup."""
    # Make sure future statements in our doctests match the Python code.  When
    # run with 2to3, the future import gets removed and these names are not
    # defined.
    try:
        testobj.globs['absolute_import'] = absolute_import
        testobj.globs['print_function'] = print_function
        testobj.globs['unicode_literals'] = unicode_literals
    except NameError:
        pass
    # Ensure that environment variables affecting translation are neutralized.
    for envar in ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG'):
        if envar in os.environ:
            del os.environ[envar]


def additional_tests():
    "Run the doc tests (README.txt and docs/*, if any exist)"
    doctest_files = [
        os.path.abspath(resource_filename('flufl.i18n', 'README.rst'))]
    if resource_exists('flufl.i18n', 'docs'):
        for name in resource_listdir('flufl.i18n', 'docs'):
            if name.endswith('.rst'):
                doctest_files.append(
                    os.path.abspath(
                        resource_filename('flufl.i18n', 'docs/%s' % name)))
    kwargs = dict(module_relative=False,
                  optionflags=DOCTEST_FLAGS,
                  setUp=setup,
                  )
    atexit.register(cleanup_resources)
    return unittest.TestSuite((
        doctest.DocFileSuite(*doctest_files, **kwargs)))
