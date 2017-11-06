# -*- coding:utf-8 -*-
import tornado.web
from model import Assignment as ag

class BaseHandler(tornado.web.RequestHandler):
    pass

class LoginHandler(BaseHandler):
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
