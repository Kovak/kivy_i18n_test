======================================================
flufl.i18n - A high level API for internationalization
======================================================

This package provides a high level, convenient API for managing
internationalization translation contexts in Python application.  There is a
simple API for single-context applications, such as command line scripts which
only need to translate into one language during the entire course of their
execution.  There is a more flexible, but still convenient API for
multi-context applications, such as servers, which may need to switch language
contexts for different tasks.


Requirements
============

``flufl.i18n`` requires Python 2.6.5 or newer, and is compatible with Python 3.


Documentation
=============

A `simple guide`_ to using the library is available within this package, in
the form of doctests.  The manual is also available online in the Cheeseshop
at:

    http://packages.python.org/flufl.i18n


Project details
===============

The project home page is:

    http://launchpad.net/flufl.i18n

You should report bugs at:

    http://bugs.launchpad.net/flufl.i18n

You can download the latest version of the package either from the Cheeseshop:

    http://pypi.python.org/pypi/flufl.i18n
    
or from the Launchpad page above.  Of course you can also just install it with
``pip`` or ``easy_install`` from the command line::

    % sudo pip flufl.i18n
    % sudo easy_install flufl.i18n

You can grab the latest development copy of the code using Bazaar, from the
Launchpad home page above.  See http://bazaar-vcs.org for details on the
Bazaar distributed revision control system.  If you have Bazaar installed, you
can branch the code like this::

     % bzr branch lp:flufl.i18n

You may contact the author via barry@python.org.


Copyright
=========

Copyright (C) 2009-2012 Barry A. Warsaw

This file is part of flufl.i18n

flufl.i18n is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

flufl.i18n is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
details.

You should have received a copy of the GNU Lesser General Public License along
with flufl.i18n.  If not, see <http://www.gnu.org/licenses/>.


Table of Contents
=================

.. toctree::
    :glob:

    docs/using
    docs/*
    NEWS

.. _`simple guide`: docs/using.html
