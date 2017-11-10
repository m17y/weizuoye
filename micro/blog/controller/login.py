# -*- coding:utf-8 -*-
import hashlib

import tornado.web
from model import Assignment as ag
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        st = ag.User()
        kwargs = dict((k,v[-1]) for k,v in self.request.arguments.items())
        kwargs['password']  =  hashlib.md5(kwargs.get('password','')).hexdigest()
        print kwargs
        st.modelfactory(kwargs)
        status,msg = st.login_verfiy()
        self.write(dict(status=status,msg=msg))
