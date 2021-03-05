import os
from pathlib import Path

from django.core.management.utils import get_random_secret_key

import cloudinary
from decouple import config

IS_CI = os.environ.get('CI', False)
BASE_DIR = Path(__file__).resolve().parent.parent

if IS_CI:
    DEBUG = True
    SECRET_KEY = get_random_secret_key()
else:
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'taggit',
    'cloudinary',
    'corsheaders',
    'debug_toolbar',
    'rest_framework',
    'taggit_serializer',
]

LOCAL_APPS = [
    'user.apps.UserConfig',
    'blog.apps.BlogConfig',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'qwoo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'qwoo.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'user.User'

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

if IS_CI:
    CACHE_DEFAULT_OPTIONS = {
        'CLIENT_CLASS': 'django_redis.client.DefaultClient',
    }
else:
    CACHE_DEFAULT_OPTIONS = {
        'PASSWORD': config('REDIS_PASSWORD'),
        'CLIENT_CLASS': 'django_redis.client.DefaultClient',
    }

CACHES = {
    'default': {
        'OPTIONS': CACHE_DEFAULT_OPTIONS,
        'LOCATION': 'redis://127.0.0.1:6379/0',
        'BACKEND': 'django_redis.cache.RedisCache',
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / 'staticfiles']

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

# Third party config

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

if IS_CI:
    GOOGLE_OAUTH2_KEY = os.environ['GOOGLE_OAUTH2_KEY']
    cloudinary.config(
        api_key=os.environ['CLOUDINARY_KEY'],
        cloud_name=os.environ['CLOUDINARY_NAME'],
        api_secret=os.environ['CLOUDINARY_SECRET'],
    )
else:
    GOOGLE_OAUTH2_KEY = config('GOOGLE_OAUTH2_KEY')
    cloudinary.config(
        api_key=config('CLOUDINARY_KEY'),
        cloud_name=config('CLOUDINARY_NAME'),
        api_secret=config('CLOUDINARY_SECRET'),
    )

TAGGIT_CASE_INSENSITIVE = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

INTERNAL_IPS = [
    '127.0.0.1',
]
