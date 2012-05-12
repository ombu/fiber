"""
Internal shared-state variables such as config settings
The top level is Fabric's env. Fiber adds its own key `fiber` to this dict
"""

import os, ConfigParser
from fabric.api import env
from fabric.utils import _AttributeDict

# Read config
config = ConfigParser.ConfigParser()
config.read('fiber_config.ini')

# AWS Credentials
os.environ['AWS_ACCESS_KEY_ID'] = config.get('ec2', 'access_key')
os.environ['AWS_SECRET_ACCESS_KEY'] = config.get('ec2', 'secret_key')

if not env.has_key('fiber'):
    env.fiber = _AttributeDict()

_ec2 = _AttributeDict(config.items('ec2'))
# type adjustments
_ec2.security_groups = _ec2.security_groups.split(',')
_ec2.region = int(_ec2.region)
env.fiber.ec2 = _ec2
