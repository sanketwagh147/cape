# region				-----External Imports-----
import os
# endregion

# region				-----Internal Imports-----
from .django import *
from .project import *
from .third_party import *
# endregion

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE'),
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'sslmode': 'require'
        },
    }
}

# CACHE

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'rediss://{os.environ.get("REDIS_HOST","127.0.0.1")}:{os.environ.get("REDIS_PORT",6379)}/1',
    }
}

MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware'] + \
             MIDDLEWARE + \
             ['django.middleware.cache.FetchFromCacheMiddleware',
              'whitenoise.middleware.WhiteNoiseMiddleware']

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

print(">>> START PROJECT WITH PROD SETTINGS <<<")
