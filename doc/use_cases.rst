=========
Use Cases
=========

Deploy a Redmine site on a new server
=====================================

Launch a server with the Redmine profile
----------------------------------------

Configure ``fiber`` and launch the server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

    [ec2]
    access_key = SETME
    secret_key = SETME
    key_filename = /path/to/your/ssh/my_key
    ami_id = ami-XYZ
    instance_type = t1.micro
    api_wait = 10
    ; int. see boto.ec2.regions
    region = 5
    ; redundant. needs to be removed
    key_name = my_key
    security_groups = webserver
    user = ombu
    webserver_user = www-data
    port = 4321
 
.. code-block:: python

    from fiber import profiles
    import fiber.profiles.redmine
    from fiber.api import launch

    fiber.bootstrap()
    server = launch('my-instance')
    profiles.redmine.install(server)
    OR
    profiles.drupal.install(server)

Create a :ref:`rocket_profile` and deploy the site
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    $ cd ~/my-redmine-site-repo
    $ fab deploy

Deploy a new site on an existing server
=======================================

Append site config to the :ref:`vakap_manifest`:

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
