#!/usr/bin/env python

import tornado.web
from model import Assignment as ag
from base import BaseHandler,context

class HomeHandler(BaseHandler):

    @context.check_permission("view", "article", message="can not view")
    def get(self):
        # import pdb;pdb.set_trace()
        print id(context),self.role
        st = ag.User()
        self.render("home.html")
