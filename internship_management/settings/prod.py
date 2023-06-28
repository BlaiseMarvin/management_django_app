import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# Application definition



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUDINARY_CLOUD_NAME'],
    'API_KEY':os.environ['CLOUDINARY_API_KEY'],
    'API_SECRET': os.environ['CLOUDINARY_API_SECRET']
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['PROD_DATABASE_NAME'],
        'USER': os.environ['PROD_DATABASE_USER'],
        'HOST': os.environ['PROD_DATABASE_HOST'],
        'PORT': os.environ['PROD_DATABASE_PORT'],
        'PASSWORD':os.environ['PROD_DATABASE_PASSWORD']
    }
}

ALLOWED_HOSTS = []


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'