from .common import *
from dotenv import dotenv_values
import cloudinary_storage


config=dotenv_values(".env")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(1wqd@b0&r2)31!*mt$ax3+k7xbz58dfgd=!+tpg_q_c1#0f(('

# Application definition


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config['CLOUDINARY_CLOUD_NAME'],
    'API_KEY': config['CLOUDINARY_API_KEY'],
    'API_SECRET': config['CLOUDINARY_API_SECRET']
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

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

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'