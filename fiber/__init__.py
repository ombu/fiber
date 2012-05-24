"""
See `fiber.api` for the publically importable API.
"""
import ConfigParser
from fiber.api import env

def bootstrap():
    import ConfigParser
    from fiber.api import env, launch
    from fiber import profiles
    import fiber.profiles.redmine

    # Read config
    config = ConfigParser.ConfigParser()
    config.read('config.ini')

    # Fab & server setup
    env.use_ssh_config = True
    env.forward_agent = True
    env.key_filename = config.get('ec2', 'key_filename')
    env.user = config.get('ec2', 'user');
    env.host_webserver_user = config.get('ec2', 'webserver_user')
    env.port = config.get('ec2', 'port')
