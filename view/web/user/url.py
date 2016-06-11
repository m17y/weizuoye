# -*- coding: utf-8 -*-
'''
Created on 2016��6��10��

@author: Su
'''
import settings
import tornado.web
from web.user.UserHandler import UserHandler
class UserApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", UserHandler),
            (r"/auth/create",UserHandler)
        ]
        super(UserApplication, self).__init__(handlers, **settings.settings)