==================
djangocms-themata
==================

A set of Bootstrap themes for Django CMS projects.

Installation
============

Install with pip from PyPI:

.. code-block:: bash

    pip install djangocms-themata

Or install directory from Github:

.. code-block:: bash

    pip install git+https://github.com/rbturnbull/djangocms-themata


Usage
========

Start with a Django project set up with `Django CMS <https://docs.django-cms.org/en/latest/introduction/01-install.html>`_.

Add ``djangocms_themata`` to the list of plugins:

.. code-block:: python

    INSTALLED_APPS += [
        "cms_bootstrap",    
        "djangocms_themata",
    ]

Migrate the database.

.. code-block:: bash

    python manage.py migrate

Get your templates to extend ``base.html``:

.. code-block:: jinja2

    {% extends "base.html" %}

Then navigate to the admin section of the website and go to the djangocms-themata section. Activate the theme that you like there.

Credits
========

App designed by Robert Turnbull (Melbourne Data Analytics Platform)

All bootstrap themes are taken from the bootswatch CDN.

