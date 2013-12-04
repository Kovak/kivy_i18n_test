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

"""Translation registry."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'registry',
    ]


from flufl.i18n._application import Application



class Registry:
    """A registry of application translation lookup strategies."""
    def __init__(self):
        # Map application names to Application instances.
        self._registry = {}

    def register(self, strategy):
        """Add an association between an application and a lookup strategy.

        :param strategy: An application translation lookup strategy.
        :type application: A callable object with a .name attribute
        :return: An application instance which can be used to access the
            language catalogs for the application.
        :rtype: `Application`
        """
        application = Application(strategy)
        self._registry[strategy.name] = application
        return application



registry = Registry()
