import tornado.web

from controller import *

class Application(tornado.web.Application):
    handlers = [
            (r"/", HomeHandler),
            (r"/login", LoginHandler),
            (r"/reg", RegHandler),
            (r"/viewtask",TaskHandler),
            (r"/users",UserHandler),
        ]