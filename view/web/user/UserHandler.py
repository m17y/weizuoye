# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
from bson.json_util import dumps
from tornado import gen
import concurrent.futures
import sys
import tornado.web
from until import Md5Encrypt
from mongo.AssignmentDao import AssignmentDao
from until.jsonFactory import MyJson
reload(sys)  
sys.setdefaultencoding('utf8') 
# A thread pool to be used for password hashing with bcrypt.
executor = concurrent.futures.ThreadPoolExecutor(2)
def any_author_exists(name):
        asgdao = AssignmentDao()
        return asgdao.find_by_name(name)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id: return None
        return user_id
class Homehandler(BaseHandler):
    def get(self):
        self.render("index.html")
class AuthCreateHandler(BaseHandler):
    def get(self):
        self.render("assignment/create_author.html")
    @gen.coroutine
    def post(self):
        print"test"
        name  = self.get_argument("name")
        email = self.get_argument("email")
        if any_author_exists(name):
            raise tornado.web.HTTPError(400, "author already created")
        hashed_password = Md5Encrypt.date_encrypt(self.get_argument("password"))
        print email
        asgdao = AssignmentDao()
        user_id = asgdao.create_local_auth(hashed_password, email, name)
        self.set_secure_cookie("user", str(user_id))
        self.render("index.html")
class LocalAuthLoginHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            self.redirect("/")
            return
        self.render("login.html",error="") 
    def post(self):
        email = self.get_argument("email")
        asgdao = AssignmentDao()
        author = asgdao.find_by_email(email)
        args = {'a': 1, 'b': 2}
        author_obj = MyJson(**author)
        print author_obj
        
        if not author:
            self.render("login.html",error="用户登录信息错误")
        hashed_password = Md5Encrypt.date_encrypt(self.get_argument("password"))
        print author
        if hashed_password == author_obj.password:
            self.set_secure_cookie("user", str(author_obj.user_id))
            self.redirect(self.get_argument("next", "/"))
        else:
            self.render("login.html",error="用户登录信息错误")
class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/auth/login"))

#        self.redirect(self.get_argument("next", "/"))
#if __name__ == "__main__":
#    email = "test"
#    name = "name"
#    hashed_password = "hashed_password"
#    asgdao = AssignmentDao()
#    asgdao.create_local_auth(hashed_password, email, name)