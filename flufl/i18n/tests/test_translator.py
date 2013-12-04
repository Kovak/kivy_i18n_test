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

"""Tests for the Translator class.

This cannot be a doctest because of the sys._getframe() manipulations.  That
does not play well with the way doctest executes Python code.  But see
translator.txt for a description of how this should work in real Python code.
"""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    ]


import unittest

from flufl.i18n._translator import Translator

# Some globals for following tests.
purple = 'porpoises'
magenta = 'monkeys'
green = 'gerbil'



class Catalog:
    """Test catalog."""

    def __init__(self):
        self.translation = None

    def ugettext(self, original):
        """Return the translation."""
        return self.translation

    # For Python 3.
    gettext = ugettext

    def charset(self):
        """Return the encoding."""
        # The default is ascii.
        return None



class TranslatorTests(unittest.TestCase):
    """Tests of the Translator class."""

    def setUp(self):
        self.catalog = Catalog()
        # We need depth=1 because we're calling the translation at the same
        # level as the locals we care about.
        self.translator = Translator(self.catalog, depth=1)

    def test_locals(self):
        # Test that locals get properly substituted.
        aqua = 'aardvarks'
        blue = 'badgers'
        cyan = 'cats'
        self.catalog.translation = '$blue and $cyan and $aqua'
        self.assertEqual(self.translator.translate('source string'),
                         'badgers and cats and aardvarks')

    def test_globals(self):
        # Test that globals get properly substituted.
        self.catalog.translation = '$purple and $magenta and $green'
        self.assertEqual(self.translator.translate('source string'),
                         'porpoises and monkeys and gerbil')

    def test_dict_overrides_locals(self):
        # Test that explicit mappings override locals.
        aqua = 'aardvarks'
        blue = 'badgers'
        cyan = 'cats'
        overrides = dict(blue='bats')
        self.catalog.translation = '$blue and $cyan and $aqua'
        self.assertEqual(self.translator.translate('source string', overrides),
                         'bats and cats and aardvarks')

    def test_globals_with_overrides(self):
        # Test that globals with overrides get properly substituted.
        self.catalog.translation = '$purple and $magenta and $green'
        overrides = dict(green='giraffe')
        self.assertEqual(self.translator.translate('source string', overrides),
                         'porpoises and monkeys and giraffe')

    def test_empty_string(self):
        # The empty string is always translated as the empty string.
        self.assertEqual(self.translator.translate(''), '')

    def test_dedent(self):
        # By default, the translated string is always dedented.
        aqua = 'aardvarks'
        blue = 'badgers'
        cyan = 'cats'
        self.catalog.translation = """\
        These are the $blue
        These are the $cyan
        These are the $aqua
        """
        for line in self.translator.translate('source string').splitlines():
            self.assertTrue(line[:5], 'These')

    def test_no_dedent(self):
        # You can optionally suppress the dedent.
        aqua = 'aardvarks'
        blue = 'badgers'
        cyan = 'cats'
        self.catalog.translation = """\
        These are the $blue
        These are the $cyan
        These are the $aqua
        """
        translator = Translator(self.catalog, dedent=False)
        for line in translator.translate('source string').splitlines():
            self.assertTrue(line[:9], '    These')
