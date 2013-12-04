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

"""Expose sub-module names in the package namespace."""

__version__ = '1.1.1'

from flufl.i18n._expand import expand
from flufl.i18n._registry import registry
from flufl.i18n._strategy import *


def initialize(domain):
    """A convenience function for setting up translation.

    :param domain: The application's name.
    :type domain: string
    """
    strategy = SimpleStrategy(domain)
    application = registry.register(strategy)
    return application._
