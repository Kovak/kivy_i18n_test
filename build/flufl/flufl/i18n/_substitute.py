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

"""Substitutions."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'Template',
    'attrdict',
    ]


import string


_missing = object()



class Template(string.Template):
    """Match any attribute path."""
    idpattern = r'[_a-z][_a-z0-9.]*'


class attrdict(dict):
    """Follow attribute paths."""
    def __getitem__(self, key):
        parts = key.split('.')
        value = super(attrdict, self).__getitem__(parts.pop(0))
        while parts:
            value = getattr(value, parts.pop(0), _missing)
            if value is _missing:
                raise KeyError(key)
        return value
