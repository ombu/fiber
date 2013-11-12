"""
Reusable server management utilities
"""

from fabric.api import sudo


def grant_admin_permissions(path):
    sudo('chgrp admin ' + path)
    sudo('chmod g+rwx ' + path)
