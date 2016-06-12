# -*- coding: utf-8 -*-
'''
Created on 2016��6��10��

@author: Su
'''
import settings
import tornado.web
from web.user.UserHandler import AuthCreateHandler, Homehandler,\
    AuthLogoutHandler
from web.user.UserHandler import LocalAuthLoginHandler
class UserApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Homehandler),
            (r"/auth/create",AuthCreateHandler),
            (r"/auth/login", LocalAuthLoginHandler),
            (r"/logout", AuthLogoutHandler)
        ]
        super(UserApplication, self).__init__(handlers, **settings.settings)