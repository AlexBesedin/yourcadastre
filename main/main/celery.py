import os
import sys

from celery import Celery

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'main'))

from service import tasks

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')


app = Celery('main)
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(['lenta_main'])
app.autodiscover_tasks()