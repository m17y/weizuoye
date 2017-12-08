# -*- coding: utf-8 -*-

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

