=====
Vakap
=====
``vakap``: maintains your deployed sites

.. _vakap_manifest:

Vakap Manifest
==============

.. code-block:: yaml

    --- # wtf
    settings:
        gpg_key: SETME
        s3_bucket: backup.ombuweb.com
        s3_access_key: SETME
        s3_secret: SETME
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

