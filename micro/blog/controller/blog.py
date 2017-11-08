#!/usr/bin/env python

import tornado.web
from model import Assignment as ag
from logic.access import context




class BaseHandler(tornado.web.RequestHandler):

    @context.set_roles_loader
    def get(self):
        yield "staff"

    def prepare(self):
        pass
        # first_load_roles()
class HomeHandler(BaseHandler):

    @context.check_permission("view", "article", message="can not view")
    def get(self):
        print id(context)
        import pdb;pdb.set_trace()
        st = ag.User()
        self.render("home.html")
