import tornado.web
from controller.blog import *

class Application(tornado.web.Application):
    handlers = [
            (r"/", HomeHandler),
        ]