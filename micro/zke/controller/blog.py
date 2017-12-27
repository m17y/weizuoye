# -*- coding:utf-8 -*-
#!/usr/bin/env python


import tornado.web
from model import Assignment as ag
from base import AccessHandler,context
from logic.access import *



@needcheck()
class HomeHandler(AccessHandler):
    # @context.check_permission("view", "article", message="can not view")
    def get(self):
        """get"""
        print id(context),self.role
        st = ag.User()
        self.render("home.html")
    def post(self):
        print id(context),self.role
        st = ag.User()
        self.render("home.html")
