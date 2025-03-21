"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 4.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import dj_database_url

from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-6%o@kt9t+2i)vjp(a3d1$1thx(n_d=34+m*1$5n0(5ht-ogf2x'

# SECURITY WARNING: don't run with debug turned on in production!
# SECRET_KEY=your_django_secret_key
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-for-dev') 
DEBUG = True
# DEBUG = os.environ.get('DEBUG', 'False') == 'True'
# DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
# ALLOWED_HOSTS = [".vercel.app"]
# ALLOWED_HOSTS=.vercel.app,localhost

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'crispy_forms',  
    'crispy_bootstrap4',
    'django_filters',
    'ckeditor',
    'ckeditor_uploader',
    'storages',
    
  
    
    
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'your_cloud_name',
    'API_KEY': 'your_api_key',
    'API_SECRET': 'your_api_secret',
}
CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.app'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',  # Database name
#         'USER': 'postgres',  # Database username
#         'PASSWORD': 'byqJCjCELUblweItXQebeYJlamaCxqkd',  # Database password
#         'HOST': 'yamanote.proxy.rlwy.net',  # Public host (DO NOT USE `postgres.railway.internal`)
#         'PORT': '13519',  # Correct PostgreSQL port from DATABASE_PUBLIC_URL
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'amosdb',
        'USER': 'amosdb',
        'PASSWORD': 'amosamosamos',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
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

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'base/static'),  
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "media")  



STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'amosolayemi18@gmail.com' #this is the sender of the mail
EMAIL_HOST_PASSWORD = 'trrotzdchqbytcfu'

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS ={
    'default':{
        'toolbar':'full',
        'height':300,
        'width':'100%',
    },
}




