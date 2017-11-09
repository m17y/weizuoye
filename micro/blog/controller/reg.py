# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from model import Assignment as ag
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class RegHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        st = ag.User()
        args = dict((k,v[-1])for k ,v in self.request.arguments.items())
        args.password  =  hashlib.md5().update(args.get('password','')).hexdigest()
        st.modelfactory(args)
        status,msg = st.login_verfiy()
        self.writer(dict(status=status,msg=msg))

