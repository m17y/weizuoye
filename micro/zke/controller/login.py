# -*- coding:utf-8 -*-
import hashlib
import json
import tornado.web
from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



# @needcheck()
class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        #用户登陆
        name = self.get_json_argument('name')
        password = self.get_json_argument('password')
        password  =  hashlib.md5(password).hexdigest()
        user = User.objects(name=name,password=password).first()
        if user:
            self.set_secure_cookie(self._USER_ID,str(user.id))
            status,msg = True,'successs'
        else:
            status,msg = False,'fail'
        print status,msg
        self.write(dict(status=status,msg=msg))
