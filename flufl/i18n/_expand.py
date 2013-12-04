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

"""String interpolation."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'expand',
    ]


import logging
from string import Template


log = logging.getLogger('flufl.i18n')



def expand(template, substitutions, template_class=Template):
    """Expand string template with substitutions.

    :param template: A PEP 292 $-string template.
    :type template: string
    :param substitutions: The substitutions dictionary.
    :type substitutions: dict
    :param template_class: The template class to use.
    :type template_class: class
    :return: The substituted string.
    :rtype: string
    """
    try:
        return template_class(template).safe_substitute(substitutions)
    except (TypeError, ValueError):
        # The template is really screwed up.
        log.exception('broken template: %s', template)
