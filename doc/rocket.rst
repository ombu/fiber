======
Rocket
======
``rocket``: deploys your sites

.. _rocket_profile:

Rocket Profile (fabfile.py)
===========================

.. code-block:: python

    from fabric.api import task, env, cd
    from butter import drush, deploy, drupal
    from fabric.contrib import files

    env.repo_type = 'git'

    # Host settings
    @task
    def staging():
        """
        The staging server definition
        """
        env.hosts = ['ombu@paco.ombuweb.com:34165']
        env.host_type = 'staging'
        env.user = 'ombu'
        env.host_webserver_user = 'www-data'
        env.host_site_path = '/vol/main/qa/qa9'
        env.db_db = 'va2'
        env.db_user = 'phpuser'
        env.db_pw = 'meh'
        env.db_host = 'localhost'
        env.aws_key = 'SETME'
        env.aws_secret = 'SETME'

