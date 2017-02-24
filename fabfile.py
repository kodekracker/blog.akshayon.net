import os
import sys
from fabric.api import local
from livereload import Server
from datetime import datetime

# Local path configuration (can be absolute or relative to fabfile)
DEPLOY_PATH = 'output'
DEFAULT_PORT = 8080

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(deploy_path=DEPLOY_PATH))
        local('mkdir {deploy_path}'.format(deploy_path=DEPLOY_PATH))

def build():
    local('pelican -s pelicanconf.py')

def rebuild():
    clean()
    build()

def reload():
    local('pelican -r -s pelicanconf.py')

def publish():
    local('pelican -s publishconf.py')

def serve(port=DEFAULT_PORT):
    server = Server()
    server.serve(host='localhost', port=port, root=DEPLOY_PATH)

# livereload
def live_serve(port=DEFAULT_PORT):
    rebuild()
    server = Server()
    server.watch('content/', build)
    server.watch('theme/pelican-bootstrap3/', build)
    server.watch('pelicanconf.py', build)
    server.watch('publishconf.py',build)
    server.serve(host='localhost', port=port, root=DEPLOY_PATH)

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
    post_file = "content/posts/{}-{:0>2}-{:0>2}-{}.md".format(today.year,
                                                              today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(post_file, 'w') as w:
        w.write(t)
    print("Post file created => " + post_file)

# publish to github pages
def publish_github(publish_drafts=False):
    clean()
    publish()
    try:
        if os.path.exists('output/drafts'):
            if not publish_drafts:
                local('rm -rf output/drafts')
    except Exception:
        pass
    local('ghp-import -pm "(updated): site updated" output')
