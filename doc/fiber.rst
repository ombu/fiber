=====
Fiber
=====

The :ref:`fiber_manifest` is a YAML file that lives in S3. This file lists
all sites in the infrastructure with information such as:

- The host(s) it lives on
- User names, passwords, and other necessary information to back up the sites
  (used by :doc:`vakap`)
- User names, passwords, and other necessary information to deploy the sites
  (used by :doc:`rocket`)

.. _fiber_manifest:

Fiber Manifest
==============

This YAML manifest lists all sites in the infrastructure.

.. code-block:: yaml

    --- # wtf
    settings:
        # Are there any global settings?
    sites:
    - name: blog.firsttechfed.com
      components:
      - type: MysqlComponent,
        host_string: ombu@flor:34165
        db_name: ftblog
        db_user: backup
      - type: MysqlComponent,
        host_string: ombu@flor:34165
        db_name: ftblog
        db_user: backup

    - name: tpc
      components:
      - type: MysqlComponent,
        host_string: ombu@flor:34165
        db_name: ftblog
        db_user: backup

