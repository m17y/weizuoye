'''
Created on 2016-6-10

@author: Su
'''
import os
import concurrent.futures
from tornado.options import define, options
define("port", default=1994, help="run on the given port", type=int)
define("mongo", default="mongodb://suyf:19940117@115.28.72.117:2016/workonline", help=" database host")

# A thread pool to be used for password hashing with bcrypt.
executor = concurrent.futures.ThreadPoolExecutor(2)
settings = dict(
            blog_title=u"Tornado Blog",
            template_path=os.path.join(os.path.abspath("templates")),
            static_path=os.path.join(os.path.abspath("static")),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            debug=True,
        )
