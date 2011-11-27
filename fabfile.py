from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.user = 'rectangular'
env.hosts = ['rectangular.webfactional.com']

def deploy():
    code_dir = '/home/rectangular/webapps/marked_django/marked'
    with cd(code_dir):
        print(" --- Updating main portfolio django app")
        run("git pull")
        
    apache_dir = '/home/rectangular/webapps/marked_django/apache2/bin'
    with cd(apache_dir):
        print(" --- Restarting Apache")
        run("./restart")
    
    static_dir = "/home/rectangular/webapps/marked_static/"
    with cd(static_dir):
#        print(" --- Deleting old static files")
#        run("rm -rf /home/rectangular/webapps/portfolio_static/*")
        print(" --- Copying new static files")
        run("cp -rp /home/rectangular/webapps/marked_django/marked/static/* /home/rectangular/webapps/marked_static/")
