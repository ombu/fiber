"""
EC2 Instance tasks
"""
import time
from fabric.api import run, hide, env, sudo
from fabric.exceptions import NetworkError
import boto.ec2

_ec2 = env.fiber.ec2

def check_instance_state(instance, wait=10):
    """
    @instance: boto.ec2.instance
    Returns the instance ID if the state is `running`, otherwise checks again
    after `env.fiber.ec2.api_wait` seconds
    """
    instance_state = instance.state
    while (instance_state != 'running'):
        print "Instance state %s. Waiting %s seconds." % (instance_state,
                wait)
        time.sleep(wait)
        instance.update()
        instance_state = instance.state
    return instance.id

def check_connectivity(wait=10):
    """
    Returns True if can connect to the env.host__string, otherwise tries again
    after `env.fiber.ec2.api_wait` seconds
    """
    try:
        with hide('running', 'stdout', 'stderr'):
            return run('uptime').succeeded
    except NetworkError:
        print "Instance is not reachable. Waiting %d seconds." % wait
        time.sleep(wait)
        check_connectivity()

def launch():
    conn = boto.ec2.regions()[int(_ec2.region)].connect()

    res = conn.run_instances(
        _ec2.ami_id,
        key_name = _ec2.key_name,
        instance_type = _ec2.instance_type,
        security_groups = _ec2.security_groups
        )

    instance = res.instances[0]
    instance.add_tag('Name', _ec2.tag_name)
    check_instance_state(instance)
    env.host_string = env.user + '@' + instance.dns_name + ':' + env.port
    check_connectivity()
    # Temp fix for now kowing the mysql root pw for `ami-5b64361e`. Can remove
    # when we start using another ami.
    _reset_mysql_pw()
    print "ssh -p %s %s@%s" % (env.port, env.user, instance.ip_address)
    return instance

def _reset_mysql_pw():
    sudo("rm -rf /var/lib/mysql && mysql_install_db && service mysql restart " +
            "&& mysqladmin -u root password '5TtEEjRK6CH~NMJu'")
