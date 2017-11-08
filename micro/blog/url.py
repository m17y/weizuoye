import tornado.web
from controller.blog import *
from controller.login import *


class Application(tornado.web.Application):
    handlers = [
            (r"/", HomeHandler),
            (r"/login", LoginHandler),
        ]