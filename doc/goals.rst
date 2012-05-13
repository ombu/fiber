================
Goals
================

Have a 'vakap manifest' command
================================

.. code-block:: yaml

    --- # All hosts
    - host: brando
      type: m1.small
      uptime: '18:59:48 up 153 days, 13:32,  0 users,  load average: 0.28, 0.06, 0.02'
      sites:
        - futureforwardmba:
            - TgzComponent: 2012-05-08
            - MysqlComponent: 2012-05-08
        - evosus:
            ...

    - host: pinche 
      type: m1.small
      uptime: '18:59:48 up 153 days, 13:32,  0 users,  load average: 0.28, 0.06, 0.02'
      sites:
        - cclc:
            - DuplicityComponent: 2012-05-10
            - MysqlComponent: 2012-05-11

Other necessary commands
=========================

**fiber assert**
    Test that every host is set to support sites and their components as listed
    in a vakap manifest.

**fiber assert**
    Test that every host is set to support sites and their components as listed
    in a vakap manifest.

**vakap report**
    Test that every host is setup and running per a vakap manifest

Sample session
==============

Append site config to rocket's ``manifest.yml``:

.. code-block:: yaml

    --- # A site descriptor
    name: m.clcc
    components:
        - DuplicityComponent:
            host_string: ombu@pinche:34165
            site_path: /mnt/main/m.cclc
        - PostgresComponent:
            host_string: webuser@db2:34165
            db_name: cclc
            db_user: cclc_user

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
