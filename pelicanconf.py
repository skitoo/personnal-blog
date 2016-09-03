#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime


DELETE_OUTPUT_DIRECTORY = True

AUTHOR = u'Alexis Couronne'
SITENAME = u'Skitoo'
SITEURL = 'http://skitoo.net'

THEME = 'theme'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%B %Y'

DEFAULT_LANG = u'fr'
CURRENT_DATE = datetime.datetime.now()

ARTICLE_PATHS = ['articles']

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = TRANSLATION_FEED_ATOM = None

AUTHOR_SAVE_AS = CATEGORY_SAVE_AS = ARCHIVES_SAVE_AS = CATEGORIES_SAVE_AS = ARTICLE_LANG_SAVE_AS = PAGE_LANG_SAVE_AS = TAGS_SAVE_AS = False
PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

STATIC_PATHS = ['images', 'downloads']

RELATIVE_URLS = True

TEMPLATE_PAGES = {
    'journal.html': 'journal.html',
    '404.html': '404.html',
    'sitemap.html': 'sitemap.xml',
    '.htaccess': '.htaccess',
}

LINKS = SOCIAL = None

DEFAULT_PAGINATION = 10

JINJA_FILTERS = {
    'limit': lambda list, number=10: list[0:number],
}
