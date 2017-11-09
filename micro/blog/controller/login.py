# -*- coding:utf-8 -*-
import tornado.web
from model import Assignment as ag
from logic.access import *
from base import BaseHandler,context
from logic.access import *



@needcheck()
class LoginHandler(BaseHandler):
    @context.check_permission("edit", "article", message="can not view")
    def get(self):
        self.render("login.html")
    def post(self):
        st = ag.Student()
        st.name = self.get_argument('name')
        st.password = self.get_argument('password')
        print st.usercount
        if st.verfiy():
            self.render("home.html")
        else:
            self.render("login.html")
