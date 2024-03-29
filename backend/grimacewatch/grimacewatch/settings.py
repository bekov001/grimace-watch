"""
Django settings for grimacewatch project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import logging
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8p6)i2jt#dea@0+c*zj1&tf(z_uj_92v(eh##655$r^_p^m975'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


# from huey import RedisHuey
# from redis import Redis

# pool = Redis(host='ec2-52-30-0-190.eu-west-1.compute.amazonaws.com', password="p9c8e589d52533082c79c4f1da2046fc6d28ccb5ebd1bf6ce7bbb7aae9bffdbad", port=15770,  ssl=True, ssl_cert_reqs=None)
# # pool = ConnectionPool(host='ec2-52-30-0-190.eu-west-1.compute.amazonaws.com', password="p9c8e589d52533082c79c4f1da2046fc6d28ccb5ebd1bf6ce7bbb7aae9bffdbad", port=15770,  ssl=True, ssl_cert_reqs=None)
# HUEY = RedisHuey('my-app', connection_pool=pool)


import os
import ssl

# settings.py
_broker_url = f'rediss://:p9c8e589d52533082c79c4f1da2046fc6d28ccb5ebd1bf6ce7bbb7aae9bffdbad@ec2-108-128-133-91.eu-west-1.compute.amazonaws.com:11380'
HUEY = {
    'huey_class': 'huey.RedisHuey',  # Huey implementation to use.
    'name': "grimacewatch",  # Use db name for huey.
    'results': True,  # Store return values of tasks.
    'store_none': False,  # If a task returns None, do not save to results.
    'immediate': False,  # If DEBUG=True, run synchronously.
    'utc': True,  # Use UTC for all times internally.
    'blocking': True,  # Perform blocking pop rather than poll Redis.
    'connection': {
       
        # 'connection_pool': None,  # Definitely you should use pooling!
        # # ... tons of other options, see redis-py for details.
        # # huey-specific connection parameters.
        # 'read_timeout': 1,  # If not polling (blocking pop), use timeout.
        'url': _broker_url,  # Allow Redis config via a DSN.
        
    },
    # ... other settings ...
}

# HUEY = {
#     'huey_class': 'huey.RedisHuey',
#     'name': 'grimacewatch',
#     "immediate": False,
#     'connection': {
#         "ssl": True,
#         "ssl_cert_reqs":None,
#         'connection_pool': None,  # Definitely you should use pooling!
#         # ... tons of other options, see redis-py for details.

#         # huey-specific connection parameters.
#         'read_timeout': 1,  # If not polling (blocking pop), use timeout.
#         'url': "rediss://:p9c8e589d52533082c79c4f1da2046fc6d28ccb5ebd1bf6ce7bbb7aae9bffdbad@ec2-52-30-0-190.eu-west-1.compute.amazonaws.com:15770",  # Allow Redis config via a DSN.
#     },
#     'consumer': {
#         'blocking': True,  # Use blocking list pop instead of polling Redis.
#         'loglevel': logging.DEBUG,
#         'workers': 4,
#         'scheduler_interval': 1,
#         'simple_log': True,
#     },
# }

# Application definition

INSTALLED_APPS = [
     'huey.contrib.djhuey',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'rest_framework',
    'corsheaders',
    'main',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'grimacewatch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

WSGI_APPLICATION = 'grimacewatch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# import os

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": os.environ.get('REDIS_URL'),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "CONNECTION_POOL_KWARGS": {
#                 "ssl_cert_reqs": None
#             },
#         }
#     }
# }


DATABASES = {     
		'default': {
      	'ENGINE': 'django.db.backends.postgresql_psycopg2', 
      	'HOST' : 'ec2-54-246-1-94.eu-west-1.compute.amazonaws.com',
      	'NAME': ('djo13s5ucnojn'),
      	'USER': 'mepamoyclsojxk',
      	'PASSWORD':  '6867f1badf2b869aa97ef468c93bce9a78c6172f488754f224d4b276850fe5b5',
      	'PORT': '5432',
    }
}
DATABASE_URL = ""
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





import django_heroku
django_heroku.settings(locals())
