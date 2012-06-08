import os
from ConfigParser import RawConfigParser

config = RawConfigParser()
config.read('/home/chronos/settings.ini')

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
        ('Nox', 'nox@freshbooks.com'),
)

MANAGERS = ADMINS

SESSION_COOKIE_DOMAIN = config.get('cookies','SESSION_COOKIE_DOMAIN')

DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'CHRONOS_DBENGINE'),
        'NAME': config.get('databases', 'CHRONOS_DATABASE'),
        'USER': config.get('databases', 'CHRONOS_DBUSER'),
        'PASSWORD': config.get('databases', 'CHRONOS_DBPASSWORD'),
        'HOST': config.get('databases', 'CHRONOS_DBHOST'),
    },

    'schedgy': {
        'ENGINE': config.get('database', 'SCHEDGY_DBENGINE'),
        'NAME': config.get('databases', 'SCHEDGY_DATABASE'),
        'USER': config.get('databases', 'SCHEDGY_DBUSER'),
        'PASSWORD': config.get('databases', 'SCHEDGY_DBPASSWORD'),
        'HOST': config.get('databases', 'SCHEDGY_DBHOST'),
}


# TEST_DATABASE_NAME = config.get('database', 'TESTSUITE_DATABASE_NAME')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/chronos/timekeeper/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(
    os.path.abspath(os.path.dirname(__file__)),
    'static'
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
STATIC_URL = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
     '/home/chronos/timekeeper/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.get('secrets','SECRET_KEY')
# CSRF_MIDDLEWARE_SECRET = config.get('secrets', 'CSRF_MIDDLEWARE_SECRET')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

DEBUG = config.getboolean('debug','DEBUG')
TEMPLATE_DEBUG = config.getboolean('debug','TEMPLATE_DEBUG')
VIEW_TEST = config.getboolean('debug', 'VIEW_TEST')
INTERNAL_IPS = tuple(config.get('debug', 'INTERNAL_IPS').split())
if config.getboolean('debug', 'SKIP_CSRF_MIDDLEWARE'):
    MIDDLEWARE_CLASSES = tuple([x for x in list(MIDDLEWARE_CLASSES)
                                  if not x.endswith('CsrfMiddleware')])

ROOT_URLCONF = 'timekeeper.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/chronos/timekeeper/templates/'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'chronos',
    'south',
    'gunicorn',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'test@localobject.com'
EMAIL_HOST_PASSWORD = 'supersecret'
EMAIL_SUBJECT_PREFIX = '[Chronos] '
EMAIL_USE_TLS = True

AUTH_PROFILE_MODULE = 'chronos.Person'

try:
    from settings_local import *
except ImportError:
    pass
