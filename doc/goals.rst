===============================================
Commands to be implemented (merge into Roadmap)
===============================================

.. _fiber_manifest_command:

``fiber manifest`` command
==========================

Output the :ref:`fiber_manifest` with sites grouped into hosts:

.. code-block:: sh

    $ fiber manifest
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
in a :ref:`fiber_manifest`.

``vakap report`` command
========================

Test that every host is setup and running per a :ref:`fiber_manifest`.

