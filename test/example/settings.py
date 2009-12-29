# Django settings for example project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Zachary Voase', 'zacharyvoase@me.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'dev.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = '1(lavq&ib1(a+=_%(6_)njg0^y$i*2t@e3#0wl1k)zehg*$nf$'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)
ROOT_URLCONF = 'example.urls'
TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djcssmin',
)

CSSMIN_INPUT = [
    # YUI Reset CSS
    'http://yui.yahooapis.com/2.8.0r4/build/reset/reset.css',
    ## 960 Grid System
    'media/css/960/reset.css',
    'media/css/960/text.css',
    'media/css/960/grid.css',
    # Local CSS Libraries
    'media/css/*.lib.css',
]

CSSMIN_OUTPUT = 'media/css/style.min.css'


import logging

logging.root.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logging.root.addHandler(handler)
