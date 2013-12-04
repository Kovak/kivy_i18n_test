# Copyright (C) 2009-2012 by Barry A. Warsaw
#
# This file is part of flufl.i18n
#
# flufl.i18n is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, version 3 of the License.
#
# flufl.i18n is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with flufl.i18n.  If not, see <http://www.gnu.org/licenses/>.

"""Catalog search strategies."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'PackageStrategy',
    'SimpleStrategy',
    ]


import os
import gettext



class _BaseStrategy:
    """Common code for strategies."""

    def __init__(self, name):
        """Create a catalog lookup strategy.

        :param name: The application's name.
        :type name: string
        """
        self.name = name
        self._messages_dir = None

    def __call__(self, language_code=None):
        """Find the catalog for the language.

        :param language_code: The language code to find.  If None, then the
            default gettext language code lookup scheme is used.
        :type language_code: string
        :return: A `gettext` catalog.
        :rtype: `gettext.NullTranslations` or subclass
        """
        # gettext.translation() requires None or a sequence.
        languages = (None if language_code is None else [language_code])
        try:
            return gettext.translation(
                self.name, self._messages_dir, languages)
        except IOError:
            # Fall back to untranslated source language.
            return gettext.NullTranslations()


class PackageStrategy(_BaseStrategy):
    """A strategy that finds catalogs based on package paths."""

    def __init__(self, name, package):
        """Create a catalog lookup strategy.

        :param name: The application's name.
        :type name: string
        :param package: The package path to the message catalogs.  This
            strategy uses the __file__ of the package path as the directory
            containing `gettext` messages.
        :type package_name: module
        """
        super(PackageStrategy, self).__init__(name)
        self._messages_dir = os.path.dirname(package.__file__)



class SimpleStrategy(_BaseStrategy):
    """A simpler strategy for getting translations."""

    def __init__(self, name):
        """Create a catalog lookup strategy.

        :param name: The application's name.
        :type name: string
        :param package: The package path to the message catalogs.  This
            strategy uses the __file__ of the package path as the directory
            containing `gettext` messages.
        :type package_name: module
        """
        super(SimpleStrategy, self).__init__(name)
        self._messages_dir = os.environ.get('LOCPATH')
