#-*- coding:utf-8 -*-
import tornado
import json
from bson import ObjectId
from logic.access import context
from logic.access import *
from model.Assignment import *

class BaseHandler(tornado.web.RequestHandler):
    role = property(lambda self: self.get_user_role())
    uid = property(lambda self: self.get_secure_cookie("uid"))
    user = property(lambda self: self.get_user())
    user_cuorse = property(lambda self: self.get_user_cuorse())
    is_teacher = property(lambda self: self.get_user_cuorse())
    
    def set_default_headers(self):
        print self.request.headers.get("Origin", "*")
        self.set_header("Access-Control-Allow-Origin", self.request.headers.get("Origin", "*"))  # 限定请求源
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,authorization")  # 请求头
        self.set_header("Access-Control-Allow-Methods", "POST,GET")  # 限定合法的请求方式
        self.set_header("Access-Control-Allow-Credentials", "true")  # 证书
        # self.set_header("Content-type", "application/json")  # 限定请求数据格式
    def options(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", self.request.headers.get("Origin", "*"))
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS,PUT,DELETE')

    def get_user(self):
        user = User.objects(id=ObjectId(self.uid)).first()
        return user

    def get_user_cuorse(self):
        courses=Course.objects(user=ObjectId(self.user))
        return courses.to_json()
    def jg_send_msg(self,uid):
        pass

    def get_user_msg(self):
        message=Message.objects(user=ObjectId(self.user))
        return courses.to_json()

    def set_acl_role(self):
        context.set_roles_loader([self.role])
       
    def get_user_role(self):
        return 'admin'
        
    def get_json_argument(self, name, default = None):
        try:
            args = json.loads(self.request.body)
            name = unicode(name)
            if name in args:
                return args[name]
            elif default is not None:
                return default
            else:
                raise MissingArgumentError(name)
        except:
            return self.get_argument(name,default)

class AccessHandler(BaseHandler):

    def prepare(self):
        # try:
        #     check_access(self,paccess.keys())
        # except:
        #     self.send_error(403)
        # if not self.get_secure_cookie("uid",None):
        #     self.render('login.html')
        pass