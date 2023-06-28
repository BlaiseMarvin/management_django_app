import os
from .common import *
from dotenv import dotenv_values

config=dotenv_values("..env")
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
        'NAME': 'dbtest',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5000',
        'PASSWORD':'ILoveDjango'
    }
}

ALLOWED_HOSTS = []


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'