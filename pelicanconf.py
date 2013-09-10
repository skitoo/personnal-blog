#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime


DELETE_OUTPUT_DIRECTORY = True

AUTHOR = u'Alexis Couronne'
SITENAME = u'Skitoo'
SITEURL = 'http://127.0.0.1:8000'

THEME = 'theme'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%B %Y'

DEFAULT_LANG = u'fr'
CURRENT_DATE = datetime.datetime.now()

ARTICLE_DIR = 'articles'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = TRANSLATION_FEED_ATOM = None

AUTHOR_SAVE_AS = CATEGORY_SAVE_AS = TAG_SAVE_AS = ARCHIVES_SAVE_AS = CATEGORIES_SAVE_AS = TAGS_SAVE_AS = ARTICLE_LANG_SAVE_AS = PAGE_LANG_SAVE_AS = False
PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

STATIC_PATHS = ['images', 'photos', 'downloads']

RELATIVE_URLS = True

TEMPLATE_PAGES = {
    'journal.html': 'journal.html',
    #'photos.html': 'photos.html',
    '404.html': '404.html',
    'sitemap.html': 'sitemap.xml',
}

LINKS = SOCIAL = None

DEFAULT_PAGINATION = 10


def limit(list, number=10):
    return list[0:number]

JINJA_FILTERS = {
    'limit': limit,
}
