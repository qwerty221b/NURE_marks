"""
Django settings for NURE_marks_engine project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2nn#j#uut-(4a*ghb%04urb@+aphyysy*az6fiy4+@jz!56b1h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'smart_selects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'NURE_marks',
    # 'import_export',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NURE_marks_engine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'NURE_marks_engine.wsgi.application'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'qwerty221b.pythonanywhere.com']
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'NURE_marks/static')

MEDIA_URL = 'propertyInfo/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'NURE_marks/media')

# ----------------------for foreign key to User:
# AUTH_USER_MODEL = 'users.CustomUser'

# ----------------------Django import-export:
# IMPORT_EXPORT_USE_TRANSACTIONS = True

# ----------------------Батарейка аутентификации:
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',

    # 'allauth' specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'

# SOCIALACCOUNT_ADAPTER = 'login.adapters.SocialAccountAdapter'

# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_EMAIL_REQUIRED = True
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# ACCOUNT_AUTHENTICATION_METHOD = 'email'

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = False
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_ADAPTER = "NURE_marks.adapters_for_Google_API.MySocialAccount"
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = True
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_USERNAME_REQUIRED = False
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# SOCIALACCOUNT_QUERY_EMAIL = True
#
# # SOCIALACCOUNT_PROVIDERS = {
# #     'google':
# #         {'SCOPE': ['profile', 'email', 'https://www.googleapis.com/auth/userinfo.email'],
# #          'AUTH_PARAMS': {
# #              'access_type': 'online'
# #          }
# #          }
# # }
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_AUTHENTICATION_METHOD = "email"
#
# ACCOUNT_EMAIL_REQUIRED = True

USE_DJANGO_JQUERY = True


