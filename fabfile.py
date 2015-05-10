from fabric.api import *
import fabric.contrib.project as project
import os
import sys
import SimpleHTTPServer
import SocketServer
import livereload
from datetime import datetime

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'


def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    os.chdir(env.deploy_path)

    PORT = 8000
    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

# A code to create entry page for new post
TEMPLATE = """
Title: {title}
Menulabel: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Modified: {year}-{month}-{day} {hour}:{minute:02d}
Category:
Tags:
Slug: {slug}
Author:
Status: draft
Summary:

"""

# TEMPLATE is declared before hand, and all the necessary imports made
def new_post(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/posts/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)

# livereload
def live_build(port=8080):

    local('make clean')
    local('make html')
    os.chdir('output')
    server = livereload.Server()
    server.watch('../content/',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('../../pelican-bootstrap3/',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('*.html')
    server.watch('*.css')
    server.watch('../pelicanconf.py',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.watch('../publishconf.py',
        livereload.shell('pelican -s ../pelicanconf.py -o ../output'))
    server.serve(liveport=35729, port=port)

# enter DNS File
def enter_dns_file(DNS=None):
    with open('output/CNAME', 'w') as f:
        f.write(DNS)

# publish to github pages
def publish_github(publish_drafts=False, dns=None):

    # clean the DEPLOY_PATH
    clean()

    # create output for publish
    local('pelican -s publishconf.py')

    try:
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')

        if dns:
            enter_dns_file(dns)

    except Exception:
        pass
    local('cp .gitignore output/')
    local('ghp-import -m "(updated): site updated" output')
    local('git push origin gh-pages:master')

    # clean the DEPLOY_PATH
    clean()
