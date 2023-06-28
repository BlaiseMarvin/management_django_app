import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# Application definition



CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config['CLOUDINARY_CLOUD_NAME'],
    'API_KEY': config['CLOUDINARY_API_KEY'],
    'API_SECRET': config['CLOUDINARY_API_SECRET']
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['PROD_DATABASE_NAME'],
        'USER': config['PROD_DATABASE_USER'],
        'HOST': config['PROD_DATABASE_HOST'],
        'PORT': config['PROD_DATABASE_PORT'],
        'PASSWORD':config['PROD_DATABASE_PASSWORD']
    }
}

ALLOWED_HOSTS = []


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'