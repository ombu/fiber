=========
Use Cases
=========

Deploy a Redmine site on a new server
=====================================

Launch a server with the Redmine profile
----------------------------------------

Configure ``fiber`` in config.ini

.. include:: fiber_config_ini.rst

Launch the server

.. code-block:: sh

    $ fiber launch --name redmine --instance-type t1.micro

The name will be the Puppet manifest to launch. It will also be use to set
the AWS Name tag.

Add the site to the :ref:`fiber_manifest`
-----------------------------------------

.. code-block:: yaml
   :emphasize-lines: 3-12

    sites:
    ...
    - name: tickets.ombuweb.com
      components:
      - type: MysqlComponent,
        host_string: pepe
        db_name: tickets
        db_user: tickets
        db_pw: secret
      - type: FileComponent,
        host_string: pepe
        site_path: /mnt/uploads

Deploy the site
---------------

.. todo::
    Add sample ``fabfile``

.. code-block:: sh

    $ cd ~/my-redmine-site
    $ fab deploy

Deploy a new site on an existing server
=======================================

Add the to the :ref:`fiber_manifest`:

.. include:: vakap_manifest_snippet.rst

Ensure the infrastructure exists to support the new site and deploy:

.. code-block:: sh

    $ fiber assert
    Site not found `m.cclc`. Would you like to setup the environment? (Y/n)
    Y
    Environment setup. You can now deploy the site.

Create a ``rocket manifest`` for your site, then:

.. code-block:: sh

    $ cd ~/my-sites/my-site
    $ rocket deploy
    $ fiber assert
    OK

Deploy a Python Webapp server
=============================

Configure ``fiber`` in config.ini

.. include:: fiber_config_ini.rst

Launch the server

.. code-block:: sh

    $ fiber launch --name django --instance-type m1.small

