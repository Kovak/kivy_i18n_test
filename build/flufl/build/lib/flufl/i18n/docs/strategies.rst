==================
Catalog strategies
==================

The way ``flufl.i18n`` finds its catalog for an application is extensible.
These are called *strategies*.  ``flufl.i18n`` comes with a couple of fairly
simple strategies.  The first locates catalog files from within a package's
directory.  Inside the package directory, you still need the ``gettext``
standard layout of ``<code>/LC_MESSAGES/<application>.mo``.


Python package strategies
=========================

For example, to use the catalog in ``flufl.i18n``'s testing package, you would
use the ``PackageStrategy``.

    >>> from flufl.i18n import PackageStrategy
    >>> import flufl.i18n.testing.messages

By setting the ``$LANG`` environment variable, we can specify that the
application translates into that language automatically.

    >>> # The testing 'xx' language rot13's the source string.
    >>> import os
    >>> os.environ['LANG'] = 'xx'

The first argument is the application name, which must be unique among all
registered strategies. The second argument is the package in which to search.

    >>> strategy = PackageStrategy('flufl', flufl.i18n.testing.messages)

Once you have the desired strategy, register this with the global registry.
The registration process returns an application object which can be used to
look up language codes.

    >>> from flufl.i18n import registry
    >>> application = registry.register(strategy)

The application object keeps track of a current translation catalog, and
exports a method which you can bind to the 'underscore' function in your
module globals for convenient gettext usage.

    >>> _ = application._

By doing so, at run time, ``_()`` will always translate the string argument to
the current catalog's language.

    >>> print(_('A test message'))
    N grfg zrffntr

..
    >>> # Hack to unregister the previous strategy.
    >>> registry._registry.clear()


Simple strategy
===============

There is also a simpler strategy that uses both the ``$LANG`` environment
variable, and the ``$LOCPATH`` environment variable to set things up::

    >>> os.environ['LOCPATH'] = os.path.dirname(
    ...     flufl.i18n.testing.messages.__file__)

    >>> from flufl.i18n import SimpleStrategy
    >>> strategy = SimpleStrategy('flufl')
    >>> application = registry.register(strategy)

    >>> _ = application._
    >>> print(_('A test message'))
    N grfg zrffntr


Calling with zero arguments
===========================

Strategies should be prepared to accept zero arguments when called, to produce
a *default* translation (usually the ``gettext.NullTranslator``).  Here, we
look for the `ugettext()` method for Python 2 and the `gettext()` method for
Python 3::

    >>> def get_ugettext(strategy):
    ...     catalog = strategy()
    ...     try:
    ...         return catalog.ugettext
    ...     except AttributeError:
    ...         # Python 3
    ...         return catalog.gettext

    >>> print(get_ugettext(SimpleStrategy('example'))('A test message'))
    A test message

    >>> print(get_ugettext(PackageStrategy(
    ...     'example', flufl.i18n.testing.messages))('A test message'))
    A test message
