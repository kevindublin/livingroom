#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kevin Dublin'
SITENAME = 'The Living Room'
SITEURL = 'https://thelivingroomsf.com'

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Make into Static Site with Secondary Blog
ARTICLE_PATHS = ['events']
ARTICLE_URL = 'events/{slug}.html'
ARTICLE_SAVE_AS = 'events/{slug}.html'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = 'events/category/{slug}.html'
CATEGORY_URL = 'events/category/{slug}.html'
TAG_SAVE_AS = 'events/tag/{slug}.html'
TAG_URL = 'events/tag/{slug}.html'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False


# Plugins Settings
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Static Paths
STATIC_PATHS = ['static', 'static/images', 'static/css', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Theme Settings
THEME = 'themes/attila'

## used for OG tags and Twitter Card data on index page
# SITEIMAGE = 'site-cover.jpg'

## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'The Living Room Reading Series and Salon, a San Franciso space for writing and conversation.'

## path to favicon
FAVICON = 'static/images/favicon.ico'

## path to logo for nav menu (optional)
LOGO = 'static/images/logo.png'

# Theme Specific Settings
HEADER_COVER = 'static/images/header.png'
# CSS_OVERRIDE = 
# HEADER_COLOR = 'black'
COLOR_SCHEME_CSS = 'darkly.css'

# Blogroll
LINKS = (("Manny's", "https://welcometomannys.com/"),
         )

# Social widget
SOCIAL = (('instagram', 'https://www.instagram.com/livingroom_sf/'),
          ('twitter', 'https://www.twitter.com/livingroom_sf/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
MAILER_LITE = True
