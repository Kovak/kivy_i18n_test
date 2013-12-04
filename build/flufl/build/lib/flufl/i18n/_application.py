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

"""An application."""

from __future__ import absolute_import, print_function, unicode_literals

__metaclass__ = type
__all__ = [
    'Application',
    ]


from flufl.i18n._translator import Translator



class _Using:
    """Context manager for _.using()."""

    def __init__(self, application, language_code):
        self._application = application
        self._language_code = language_code

    def __enter__(self):
        self._application.push(self._language_code)

    def __exit__(self, *exc_info):
        self._application.pop()
        # Do not suppress exceptions.
        return False



class _Underscore:
    """The implementation of the _() function.

    This class is internal representation only and has an incestuous
    relationship with the Application class.
    """

    def __init__(self, application):
        self._application = application

    def __call__(self, original, extras=None):
        """Translate the string into the language of the current context.

        :param original: The original string to translate.
        :type original: string
        :param extras: Extra substitution mapping, elements of which override
            the locals and globals.
        :return: The translated string.
        :rtype: string
        """
        return self._application.current.translate(original, extras)

    def using(self, language_code):
        """Create a context manager for temporary translation.

        While in this context manager, translations use the given language
        code.  When the with statement exits, the original language is
        restored.  These are nestable.
        """
        return _Using(self._application, language_code)

    def push(self, language_code):
        """Push a new catalog onto the stack.

        The translation catalog associated with the language code now becomes
        the currently active translation context.
        """
        self._application.push(language_code)

    def pop(self):
        """Pop the current catalog off the translation stack.

        No exception is raised for under-runs.  In that case, pop() just
        no-ops and the null translation becomes the current translation
        context.
        """
        self._application.pop()

    @property
    def default(self):
        """Return the default language code.

        :return: The default language code.
        :rtype: string or None if there is no default language
        """
        return self._application.default

    @default.setter
    def default(self, language_code):
        """Set the default language code.

        :param language_code: The language code for the default translator.
        :type language_code: string
        """
        self._application.default = language_code

    @default.deleter
    def default(self):
        """Reset the default language to the null translator."""
        del self._application.default

    @property
    def code(self):
        """Return the language code currently in effect."""
        code = self._application.code
        if code is None:
            return self.default
        return code



class Application:
    """Manage all the catalogs for a particular application.

    You can ask the application for a specific catalog based on the language
    code.  The Application requires a strategy for finding catalog files.

    Attributes:

    * dedent (default True) - controls whether translated strings are dedented
      or not.  This is passed through to the underlying `Translator`
      instance.
    * depth (default 2) - The number of stack frames to call sys._getframe()
      with in the underlying `Translator` instance.  Passed through to that
      class's constructor.
    """
    def __init__(self, strategy):
        """Create an `Application`.

        Use the `dedent` attribute on this instance to control whether
        translated strings are dedented or not.  This is passed straight
        through to the `Translator` instance created in the _() method.

        :param strategy: A callable that can find catalog files for the
            application based on the language code.
        :type strategy: callable taking one string argument, the language code.
        """
        self._strategy = strategy
        # A mapping from language codes to catalogs.
        self._catalogs = {}
        self._stack = []
        # Arguments to the Translator constructor.
        self.dedent = True
        self.depth = 2
        # By default, the baseline translator is the null translator.  Use our
        # public API so that we share code.
        self._default_language = None
        self._default_translator = None
        # This sets the _default_translator.
        del self.default

    @property
    def name(self):
        """The application name.

        :return: The application name.
        :rtype: string
        """
        return self._strategy.name

    @property
    def default(self):
        """Return the default language code.

        :return: The default language code.
        :rtype: string or None if there is no default language
        """
        return self._default_language

    @default.setter
    def default(self, language_code):
        """Set the default language code.

        :param language_code: The language code for the default translator.
        :type language_code: string
        """
        self._default_language = language_code
        catalog = self.get(language_code)
        self._default_translator = Translator(catalog, self.dedent, self.depth)

    @default.deleter
    def default(self):
        """Reset the default language to the null translator."""
        self._default_language = None
        self._default_translator = Translator(
            self._strategy(), self.dedent, self.depth)

    def get(self, language_code):
        """Get the catalog associated with the language code.

        :param language_code: The language code.
        :type language_code: string
        :return: A `gettext` catalog.
        :rtype: `gettext.NullTranslations` or subclass.
        """
        missing = object()
        catalog = self._catalogs.get(language_code, missing)
        if catalog is missing:
            catalog = self._strategy(language_code)
            self._catalogs[language_code] = catalog
        return catalog

    @property
    def _(self):
        """Return a translator object, tied to the current catalog.

        :return: A translator context object for the current active catalog.
        :rtype: `Translator`
        """
        return _Underscore(self)

    def push(self, language_code):
        """Push a new catalog onto the stack.

        The translation catalog associated with the language code now becomes
        the currently active translation context.
        """
        catalog = self.get(language_code)
        translator = Translator(catalog, self.dedent, self.depth)
        self._stack.append((language_code, translator))

    def pop(self):
        """Pop the current catalog off the translation stack.

        No exception is raised for under-runs.  In that case, pop() just
        no-ops and the null translation becomes the current translation
        context.
        """
        if len(self._stack) > 0:
            self._stack.pop()

    @property
    def current(self):
        """Return the current translator.

        :return: The current translator.
        :rtype: `Translator`
        """
        if len(self._stack) == 0:
            return self._default_translator
        return self._stack[-1][1]

    @property
    def code(self):
        """Return the current language code.

        :return: The current language code.
        :rtype: string
        """
        if len(self._stack) == 0:
            return None
        return self._stack[-1][0]
