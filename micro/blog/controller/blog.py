#!/usr/bin/env python

import tornado.web
from model import Assignment as ag

class BaseHandler(tornado.web.RequestHandler):
    pass

class HomeHandler(BaseHandler):
    def get(self):
        st = ag.Student()
        self.render("home.html")
