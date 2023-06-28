import os 
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','internship_management.settings.dev')

celery=Celery('internship_management')
celery.config_from_object('django.conf:settings',namespace='CELERY')
celery.autodiscover_tasks()

