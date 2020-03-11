######
Awards
######

An application to manage PyGotham financial aid and scholarship applications and
awards.

=============
Configuration
=============

Awards can be configured through either environment variables or a
`settings.ini` file. An `example_settings.ini` file has been provided. You can
kickstart your configuration with::

    $ cp example_settings.ini settings.ini

.. note::

    Configuration for tests should be specified in the `testenv.setenv` section
    of `tox.ini`.

=======
Testing
=======

While all tests will be as part of CI, they can also be run locally through
tox_.

----------
Unit tests
----------

The unit tests will be run whenever tox is envoked without specifying an
environment, but can be run directly with::

    $ tox -e py38

The test environment require access to a database. It's connection string must
be specified through the `DATABASE_URI_TESTS` environment variable::

    $ env DATABASE_URI_TESTS=postgresql+psycopg2://user:password@host:port/dbname tox -e py38

-------------------
Checking migrations
-------------------

You can check both that all necessary migration files have been created and
that all migrations can be run (in both directions) successfully::

    $ tox -e migrations

The tox environment require access to a database. It's connection string must
be specified through the `DATABASE_URI_MIGRATIONS` environment variable::

    $ env DATABASE_URI_MIGRATIONS=postgresql+psycopg2://user:password@host:port/dbname tox -e migrations

.. _tox: https://tox.readthedocs.io
