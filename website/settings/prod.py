# region				-----External Imports-----
from django.core.management.utils import get_random_secret_key  
import glob, os
# endregion

# region				-----Internal Imports-----
from .django import *
from .project import *
from .third_party import *
# endregion

SECRET_KEY = os.environ.get('SECRET_KEY', '')

DEBUG = False

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

DATABASES = {
    'default': {
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'PORT': os.environ.get('DATABASE_PORT'),
        'USER': os.environ.get('DATABASE_USER'),
        'ENGINE': os.environ.get('ENGINE'),
        'ATOMIC_REQUESTS': True
    }
}

# CACHE

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{os.environ.get("REDIS_HOST","127.0.0.1")}:{os.environ.get("REDIS_PORT",6379)}/1',
    }
}

MIDDLEWARE = ['django.middleware.cache.UpdateCacheMiddleware'] + \
             MIDDLEWARE + \
             ['django.middleware.cache.FetchFromCacheMiddleware']

CSRF_TRUSTED_ORIGINS = [
    f'http://{os.environ.get("BACKEND_DOMAIN")}',
    f'https://{os.environ.get("BACKEND_DOMAIN")}',
    'http://127.0.0.1:3000',
    'http://127.0.0.1',
    'http://localhost:3000',
    'http://localhost'
]

print(">>> START PROJECT WITH PROD SETTINGS <<<")
