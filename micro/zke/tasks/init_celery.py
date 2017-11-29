# file_name=init_celery.py
# coding: utf-8
from celery import Celery


BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'

celery = Celery('celery',
    broker=BROKER_URL,
    backend=BACKEND_URL,
    )

celery.conf.update(
    CELERY_ACKS_LATE=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERYD_FORCE_EXECV=True,
    CELERYD_MAX_TASKS_PER_CHILD=500,
    BROKER_HEARTBEAT=0,
)