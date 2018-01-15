# -*- coding: utf-8 -*-
from celery import Celery
import concurrent.futures
from tornado.options import define, options

define("port", default=9878, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="blog database host")
define("mysql_database", default="blog", help="blog database name")
define("mysql_user", default="blog", help="blog database user")
define("mysql_password", default="blog", help="blog database password")

#极光推送 配置
APP_KEY = '6c1657164a468894953ac402'
MASTER_SECRET = '78e4680b4847429144301c0d'
REDIS_HOST = '127.0.0.1:6379'
PUBSUB_CHANNEL = set(['base_channel','WINDPOWER-PUBSUB-CHANNEL'])

#celery配置文件
BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'

celery = Celery('tasks',
    broker=BROKER_URL,
    backend=BACKEND_URL,
    )

celery.conf.update(
    CELERY_ACKS_LATE=True,
    CELERY_IMPORTS = ('task_server'), # 指定导入的任务模块 
    CELERY_ACCEPT_CONTENT=['json'],
    CELERYD_FORCE_EXECV=True,
    CELERYD_MAX_TASKS_PER_CHILD=500,
    BROKER_HEARTBEAT=0,
)