from fabric.api import run, sudo
from fabric.utils import _AttributeDict
from fabric.contrib.files import upload_template
from fiber.api import grant_admin_permissions

conf = {
    'version': '1.4.1',
    'path':    '/home/ombu/redmine',
    'repo':    'git://github.com/redmine/redmine.git',
    'site_name':    't.ombuweb.com'
}
conf = _AttributeDict(conf)

def install(server):
    """ Install redmine on a server
    Keyword arguments:
    server -- a boto.ec2.instance
    conf   -- redmine configuration
    """

    # Dependencies
    sudo('apt-get update')
    sudo('apt-get -y install libapache2-mod-passenger ruby1.8-dev libmagickwand-dev libopenssl-ruby')
    sudo('a2enmod passenger')
    _upgrade_rubygems()
    sudo('gem install --no-ri --no-rdoc bundler')

    # Setup environment
    upload_template(
        'fiber/profiles/redmine/templates/passenger.conf',
        '/etc/apache2/mods-available/passenger.conf',
        use_sudo=True)

def _upgrade_rubygems():
    sudo('gem install rubygems-update')
    sudo('cd /var/lib/gems/1.8/bin && ./update_rubygems')
