"""
Django settings for realmind project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from django.core.management.utils import get_random_secret_key
from pathlib import Path
import os
import sys
import dj_database_url



import cloudinary
import django_heroku



#import cloudinary_storage

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%cy(6u9i(3kotxuc^&u5e^ec=nv127id5a^p)^187vrlgqh#kl'

#SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#to decide later
#DEBUG = os.getenv("DEBUG", "False") == "True"
#ALLOWED_HOSTS = ['127.0.0.1','localhost',]

#ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

ALLOWED_HOSTS = ['www.realmindt.com','realmind.com']

#DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# Application definition


#DEBUG = str(os.environ.get('DEBUG')) =="1" #1 == True

#ENV_ALLOWED_HOST = os.environ.get('DJANGO_ALLOWED_HOSTS') or None

#ALLOWED_HOSTS = []
#if not DEBUG:
 #   ALLOWED_HOSTS +=[os.environ.get('DJANGO_ALLOWED_HOST')]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'product',
    'accounts',
    'cloudinary',
    'crispy_forms',
    'django_filters'
    
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

ROOT_URLCONF = 'realmind.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR ,'templates')],
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




WSGI_APPLICATION = 'realmind.wsgi.application'



#if DEVELOPMENT_MODE is True:
  #  DATABASES = {
      #  "default": {
            #"ENGINE": "django.db.backends.sqlite3",
            #"NAME": os.path.join(BASE_DIR, "db.sqlite3"),

       # 'ENGINE': 'django.db.backends.postgresql',
       # 'USER' : 'itlzduosjtdnvo',
       # 'NAME': 'degvfa2bv0la1b',
       # 'PORT':5432,
        #'PASSWORD' :'c5e6de0d3077c06ad22e3c1c642eb8de2b66bc195bb99505a46c7ccb3ebdff73',
       # 'HOST': 'ec2-3-229-8-233.compute-1.amazonaws.com'
        #}
   # }
    
#elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
   # if os.getenv("DATABASE_URL", None) is None:
    #    raise Exception("DATABASE_URL environment variable not defined")
        
  #  DATABASES = {
   #     "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
  #  }





# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'degvfa2bv0la1b',
        'USER' : 'itlzduosjtdnvo',
        'PORT':5432,
        'PASSWORD' :'c5e6de0d3077c06ad22e3c1c642eb8de2b66bc195bb99505a46c7ccb3ebdff73',
        'HOST': 'ec2-3-229-8-233.compute-1.amazonaws.com'
    }
}
#POSTGRES_DB = os.environ.get("POSTGRES_DB") #DB name
#POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
#POSTGRES_USER = os.environ.get("POSTGRES_USER")
#POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
#POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

#POSTGRES_READY =(
#    POSTGRES_DB is not None
#     and POSTGRES_PASSWORD is not None
#     and POSTGRES_USER is not None
#     and POSTGRES_HOST is not None
#     and POSTGRES_PORT is not None
#)

#if POSTGRES_READY:
#    DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': POSTGRES_DB,
#        'USER' : POSTGRES_USER,
#        'PASSWORD' :POSTGRES_PASSWORD,
#        'HOST': POSTGRES_HOST,
#        'PORT':POSTGRES_PORT,
        
        
#    }
#}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [os.path.join(BASE_DIR ,'static') ]
STATIC_ROOT =os.path.join(BASE_DIR ,'staticfiles')  

MEDIA_URL ='/media/'
MEDIA_ROOT =os.path.join(BASE_DIR ,'media')




cloudinary.config( 
  cloud_name = "dihjcmvi3", 
  api_key = 719413493487441, 
  api_secret = "OdUEmhlZnR8xNsGrvTwh7RkPVL4" 
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field




django_heroku.settings(locals())

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER ='realmindt@gmail.com'
EMAIL_HOST_PASSWORD  = 'RealMind#@tech!*{}21.'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

