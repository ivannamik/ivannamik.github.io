#!/usr/bin/env python

AUTHOR = u'Ivanna'
SITENAME = u'ivanna.ca'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['media']

THEME = 'themes/default'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = u'en'

# Disable all feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
USE_FOLDER_AS_CATEGORY = False
LOAD_CONTENT_CACHE = False

GOOGLE_ANALYTICS = 'UA-25056700-1'

DIRECT_TEMPLATES = ['index']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

PLUGIN_PATHS = [
    'plugins',
]

PLUGINS = [
    # Download better_figures_and_images from [github] and then 
    # install its dependencies: pip install pillow beautifulsoup4
    # [github]: https://github.com/getpelican/pelican-plugins
    'better_figures_and_images',
]

