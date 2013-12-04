===================
Expanding templates
===================

`PEP 292`_ defines a simplified string template, where substitution variables
are identified by a leading ``$``-sign.  The substitution dictionary names the
keys and values that should be interpolated into the template::

    >>> key_1 = 'key_1'
    >>> key_2 = 'key_2'

    >>> from flufl.i18n import expand
    >>> # This may fail for Python < 2.6.5
    >>> print(expand(
    ...     '$key_2 is different than $key_1', {
    ...         key_1: 'the first key',
    ...         key_2: 'the second key',
    ...         }))
    the second key is different than the first key

See `issue 4978`_ for Python 2.6.x compatibility.


.. _`PEP 292`: http://www.python.org/dev/peps/pep-0292/
.. _`issue 4978`: http://bugs.python.org/issue4978
