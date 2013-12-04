=====================
NEWS for flufl.i18n
=====================

1.1.1 (2012-04-19)
==================
 * Add classifiers to setup.py and make the long description more compatible
   with the Cheeseshop.
 * Other changes to make the Cheeseshop page look nicer.  (LP: #680136)
 * setup_helper.py version 2.1.


1.1 (2012-01-19)
================
 * Support Python 3 without the need for 2to3.


1.0.4 (2010-12-06)
==================
 * Restore missing line from MANIFEST.in to fix distribution tarball.


1.0.3 (2010-12-01)
==================
 * Fix setup.py to not install myfixers artifact directory on install.
 * Remove pylint.rc; we'll use pyflakes instead.


1.0.2 (2010-06-23)
==================
 * Small documentation fix.


1.0.1 (2010-06-09)
==================
 * Ditch the use of zc.buildout.
 * Improved documentation.


1.0 (2010-04-24)
================
 * Use Distribute instead of Setuptools.
 * Port to Python 3 when used with 2to3.
 * More documentation improvements.


0.6 (2010-04-21)
================
 * Documentation and lint clean up.


0.5 (2010-04-20)
================
 * Added a simplified initialization API for one-language-context
   applications. This works much better for non-server applications.
 * Added a SimpleStrategy which recognizes the $LOCPATH environment variable.
 * Show how PEP 292 strings are supported automatically.
 * When strategies are called with zero arguments, they supply the default
   translation context, which is usually a NullTranslation.  This is better
   than hardcoding the NullTranslation in the Application.


0.4 (2010-03-04)
================
 * Add the ability to get the current language code, via _.code


0.3 (2009-11-15)
================
 * Initial release; refactored from Mailman 3.
