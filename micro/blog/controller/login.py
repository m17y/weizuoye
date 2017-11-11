# -*- coding:utf-8 -*-
import hashlib

import tornado.web
from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        st = User()
        kwargs = dict((k,v[-1]) for k,v in self.request.arguments.items())
        kwargs['password']  =  hashlib.md5(kwargs.get('password','')).hexdigest()
        print kwargs
        st.modelfactory(kwargs)
        import pdb;pdb.set_trace()
        user = User.objects(name=st.name).first()
        if user and user.password==st.password:
            self.set_secure_cookie("uid",str(user.id))
            status,msg = True,'successs'
        else:
            status,msg = False,'fail'
        self.write(dict(status=status,msg=msg))
