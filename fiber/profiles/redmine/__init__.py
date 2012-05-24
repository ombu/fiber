from fabric.api import run, sudo
from fabric.utils import _AttributeDict
from fabric.contrib.files import upload_template
from fiber.api import grant_admin_permissions

conf = {
    'version': '1.4.1',
    'path':    '/home/ombu/redmine',
    'repo':    'git://github.com/redmine/redmine.git',
    'site_name':    'rm.ombuweb.com'
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
    run('rm -rf %s && git clone %s %s' % (conf.path, conf.repo, conf.path))
    run('cd %s && git checkout %s' % (conf.path, conf.version))
    upload_template(
        'fiber/profiles/redmine/templates/passenger.conf',
        '/etc/apache2/mods-available/passenger.conf',
        use_sudo=True)
    upload_template(
        'fiber/profiles/redmine/templates/apache_vhost',
        '/etc/apache2/sites-available/redmine',
        context=conf,
        use_sudo=True)
    _set_app_permissions()
    sudo('cd %s && bundle install --without development test' % conf.path)
    sudo('a2ensite redmine && service apache2 stop && service apache2 start')

    # Configure Redmine
    _config()

def _config():
    pass

def _set_app_permissions():
    run('chmod a+x %s/public' % conf.path)

def _upgrade_rubygems():
    sudo('gem install rubygems-update')
    sudo('cd /var/lib/gems/1.8/bin && ./update_rubygems')
