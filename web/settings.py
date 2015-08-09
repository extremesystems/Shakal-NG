# -*- coding: utf-8 -*-
"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import re

from .assets import ASSETS, SPRITES


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ASSETS_MANAGER_SPRITES = SPRITES
ASSETS_MANAGER_FILES = ASSETS

SECRET_KEY = '*h4+%(b@_+-au@mmh^lp3v=^wkddzp(n63883zzm_i5xdnmb+v'

DEBUG = True

TEMPLATE_DEBUG = True

ADMINS = (('Miroslav Bendik', 'mireq@linuxos.sk'),)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'web@linuxos.sk'

ALLOWED_HOSTS = []


INSTALLED_APPS = (
	'template_dynamicloader',
	# core
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	# vendor
	'django_assets_manager',
	'django_autoslugfield',
	'django_sample_generator',
	'compressor',
	'django_jinja',
	# apps
	'accounts',
	'article',
	'attachment',
	'breadcrumbs',
	'feeds',
	'hitcount',
	'threaded_comments',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
	# custom
	'common_utils.middlewares.ThreadLocal.ThreadLocalMiddleware',
	'template_dynamicloader.middleware.TemplateSwitcherMiddleware',
	'feeds.middleware.FeedsMiddleware',
)

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
	{
		"BACKEND": "template_dynamicloader.backend.Jinja2",
		'DIRS': [os.path.join(BASE_DIR, 'templates'),],
		"OPTIONS": {
			"match_extension": None,
			"match_regex": re.compile(r"^(?!(admin/|debug_toolbar/|suit/|profiler/)).*"),
			"newstyle_gettext": True,
			"extensions": [
				"jinja2.ext.do",
				"jinja2.ext.loopcontrols",
				"jinja2.ext.with_",
				"jinja2.ext.i18n",
				"jinja2.ext.autoescape",
				"django_jinja.builtins.extensions.CsrfExtension",
				"django_jinja.builtins.extensions.CacheExtension",
				"django_jinja.builtins.extensions.TimezoneExtension",
				"django_jinja.builtins.extensions.UrlsExtension",
				"django_jinja.builtins.extensions.StaticFilesExtension",
				"django_jinja.builtins.extensions.DjangoFiltersExtension",
				"compressor.contrib.jinja2ext.CompressorExtension",
			],
			"context_processors": [
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'breadcrumbs.context_processors.breadcrumbs',
			],
			#'context_processors': TCP + (
			#	'django.core.context_processors.request',
			#	'django.contrib.auth.context_processors.auth',
			#	'django.contrib.messages.context_processors.messages',
			#	'breadcrumbs.context_processors.breadcrumbs',
			#	'feeds.context_processors.feeds',
			#	'template_dynamicloader.context_processors.style',
			#	'allauth.account.context_processors.account'
			#),
			"autoescape": True,
			"auto_reload": True,
			"translation_engine": "django.utils.translation",
		}
	},
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(BASE_DIR, 'templates'),],
		'OPTIONS': {
			'loaders': [
				'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
			],
			'context_processors': [
				#'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		},
	},
]

DYNAMIC_TEMPLATES = ('default', 'new')

CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'KEY_PREFIX': 'linuxos',
		'LOCATION': 'linuxos-default',
	},
	'jinja': {
		#'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		'KEY_PREFIX': 'jinja',
		'LOCATION': 'linuxos-jinja',
	},
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

WSGI_APPLICATION = os.environ.get('DJANGO_WSGI_APPLICATION', 'web.wsgi.application')

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	}
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'sk_SK'

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

LANGUAGES = (('sk', 'Slovak'),)

TIME_ZONE = 'Europe/Bratislava'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

FEED_SIZE = 20

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'media'))
MEDIA_URL = '/media/'

MEDIA_CACHE_DIR = os.path.join(MEDIA_ROOT, 'cache')
MEDIA_CACHE_URL = MEDIA_URL + 'cache/'

# allauth
LOGIN_URL = 'account_login'
LOGIN_REDIRECT_URL = 'account_my_profile'
ACCOUNT_FORMS = {
	'login': 'accounts.forms.LoginForm',
	'add_email': 'accounts.forms.AddEmailForm',
	'signup': 'accounts.forms.SignupForm',
}
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_ACTIVATION_DAYS = 7
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',
	'accounts.backend.AuthRememberBackend',
)

INITIAL_DATA_COUNT = {
	'user': 50,
}

SAMPLE_DATA_GENERATORS = (
	'accounts.generators.register',
	'article.generators.register',
)

JINJA2_BYTECODE_CACHE_NAME = "jinja"
JINJA2_BYTECODE_CACHE_ENABLE = False

def COMPRESS_JINJA2_GET_ENVIRONMENT():
	from django.template import engines
	return engines.all()[0].env

COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')
COMPRESS_PRECOMPILERS = (
	('text/x-scss', 'django_libsass.SassCompiler'),
)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_REBUILD_TIMEOUT = 1

LIBSASS_SOURCE_COMMENTS = False
LIBSASS_OUTPUT_STYLE = 'compressed'

from .patch_urls import patch_urls
patch_urls()
