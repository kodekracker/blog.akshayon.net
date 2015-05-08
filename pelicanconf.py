#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Akshay Pratap Singh'
SITENAME = u'#kodekracker'
SITEURL = ''

PATH = 'content'

THEME = "../pelican-bootstrap3"

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/AKSHAYPRATAP007'),
          ('Twitter', 'https://twitter.com/KodeKracker'),
          ('Google+','https://plus.google.com/+AkshayPratap_01'),
          ('Linkedin','https://in.linkedin.com/in/akshaypratapsingh'),
          ('Github','https://github.com/KodeKracker/'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../Pelican/pelican-plugins']
PLUGINS = ['gravatar', 'related_posts', 'series','tipue_search']


## Pelican Bootstrap 3 Theme

# Templete Settings
DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_MENU = False

BOOTSTRAP_THEME = "flatly"

PYGMENTS_STYLE = "tango"

BOOTSTRAP_FLUID = False

USE_PAGER = True

DISPLAY_BREADCRUMBS = True

DISPLAY_CATEGORY_IN_BREADCRUMBS = True

BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True

RELATED_POSTS_MAX = 3

RELATED_POSTS_SKIP_SAME_CATEGORY = False

DISPLAY_SERIES_ON_SIDEBAR = False

SHOW_SERIES = False

ABOUT_ME = 'Data Science Enthusiast, Web Developer and Programmer'

AVATAR = "../images/profile-pic.jpeg"

HIDE_SIDEBAR = False

TWITTER_USERNAME = 'kodekracker'

TWITTER_WIDGET_ID = os.getenv('TWITTER_WIDGET_ID',None)

TWEET_LIMIT = 3

SHARIFF = True

SHARIFF_ORIENTATION = 'horizontal'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

FAVICON = 'images/favicon.ico'
