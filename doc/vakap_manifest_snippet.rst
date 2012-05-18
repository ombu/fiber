.. code-block:: yaml

    --- # A site descriptor
    name: m.clcc.foo
    components:
        - DuplicityComponent:
            host_string: ombu@pinche:34165
            site_path: /mnt/main/m.cclc
        - PostgresComponent:
            host_string: webuser@db2:34165
            db_name: cclc
            db_user: cclc_user
