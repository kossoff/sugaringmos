# -*- coding: utf8 -*-
"""
Django settings for petrosugar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')3b_!ht6+$x$@a-8cg6315q!2(l^blf(hjn_9y15dm6kefdgnn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'sugaringmos.ru',
    'www.sugaringmos.ru',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'adminka',
    'adminka.faq',
    'adminka.prices',
    'adminka.contacts',
    'adminka.services',
    'adminka.frontpage',
    'adminka.sugarwaxing',
    'front',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'petrosugar.middleware.FullAuthMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'petrosugar.context_processors.contacts_context_processor',
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

ROOT_URLCONF = 'petrosugar.urls'

LOGIN_URL = '/adminka/'

WSGI_APPLICATION = 'petrosugar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2','mysql','sqlite3' or 'oracle'.
        'NAME': 'petrosugar',                  # Or path to database file if using sqlite3.
        'USER': 'sugawax',                     # Not used with sqlite3.
        'PASSWORD': 'Slu1ga_w4a2x',            # Not used with sqlite3.
        'HOST': '',                            # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                            # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Media files (Uploaded files)

MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = os.path.join('/var/www/sugaringmos/media/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join('/var/www/sugaringmos/static/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'templates/adminka/static'),
    os.path.join(BASE_DIR, 'templates/frontend/static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/adminka'),
    os.path.join(BASE_DIR, 'templates/adminka/faq'),
    os.path.join(BASE_DIR, 'templates/adminka/prices'),
    os.path.join(BASE_DIR, 'templates/adminka/contacts'),
    os.path.join(BASE_DIR, 'templates/adminka/services'),
    os.path.join(BASE_DIR, 'templates/adminka/frontpage'),
    os.path.join(BASE_DIR, 'templates/adminka/sugarwaxing'),
    os.path.join(BASE_DIR, 'templates/frontend'),
    #os.path.join(BASE_DIR, 'templates/homepage'),
    #os.path.join(BASE_DIR, 'templates/fieldtype'),
    #os.path.join(BASE_DIR, 'templates/enterprise'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
