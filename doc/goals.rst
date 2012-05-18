===============================================
Commands to be implemented (merge into Roadmap)
===============================================

.. _vakap_manifest_command:

``vakap manifest`` command
==========================

Output the :ref:`vakap_manifest` with sites grouped into hosts:

.. code-block:: sh

    $ vakap manifest
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

``fiber assert`` command
========================

    Test that every host is set to support sites and their components as listed
    in a :ref:`vakap_manifest`.

``vakap report`` command
========================

**vakap report**
    Test that every host is setup and running per a :ref:`vakap_manifest`.

