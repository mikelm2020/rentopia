"""
Django settings for rentopia project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import logging
import os
from pathlib import Path

import environ

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
print("E U R E K A -- BASE_DIR: " + os.path.join(BASE_DIR, ".env"))

# False if not in os.environ because of casting above
DEBUG = env("DEBUG")
print(" RED PILL:", DEBUG)

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

ALLOWED_HOSTS = []


# Application definition
# Applications core of Django
BASE_APPS = [   
    "daphne",     
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# Local applications
LOCAL_APPS = [
    "apps.booking",
    "apps.chatbot",
    "apps.geolocalization",
    "apps.messaging",
    "apps.properties",
    "apps.rating",
    "apps.upload",
    "apps.users",
]

# Third persons applications
THIRD_APPS = [      
    "channels", 
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "drf_spectacular",
    "drf_standardized_errors",    
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "rentopia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rentopia.wsgi.application"

ASGI_APPLICATION = "rentopia.asgi.application"

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
}


ADMINS = [({env("ADMIN1_NAME")}, {env("ADMIN1_EMAIL")})]

# Logging
PROPAGATE = env("PROPAGATE")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": "DEBUG",
        # Adding the watchtower handler here causes all loggers in the project that
        # have propagate=True (the default) to send messages to watchtower. If you
        # wish to send only from specific loggers instead, remove "watchtower" here
        # and configure individual loggers below.
        "handlers": ["console"],
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": ["require_debug_true"],
            "class": "logging.StreamHandler",
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        # "console": {
        #     "class": "logging.StreamHandler",
        # },
    },
    "loggers": {
        # In the debug server (`manage.py runserver`), several Django system loggers cause
        # deadlocks when using threading in the logging handler, and are not supported by
        # watchtower. This limitation does not apply when running on production WSGI servers
        # (gunicorn, uwsgi, etc.), so we recommend that you set `propagate=True` below in your
        # production-specific Django settings file to receive Django system logs in CloudWatch.
        # "django": {
        #     "level": "DEBUG",
        #     "handlers": ["console"],
        #     "propagate": PROPAGATE,
        # }
        # Add any other logger-specific configuration here.
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
            "propagate": PROPAGATE,
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": PROPAGATE,
        },
    },
}
