import tornado.web

from controller import *

class Application(tornado.web.Application):
    handlers = [
            (r"/login",LoginHandler),
            (r"/reg",UserHandler),

            (r"/user",UserHandler),
            (r"/user/reset",ResetUserHandler),

            (r"/course",CourseHandler),
            (r"/course/task",CourseTaskHandler),
            (r"/course/user",CrouseUser),

            (r"/task",TaskHandler),
            (r"/task/unfinished",TaskUnfinishedHndler),
        ]