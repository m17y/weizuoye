# -*- coding: utf-8 -*-
'''
Created on 2016年6月10日

@author: Su
'''
from tornado import gen
import concurrent.futures
import bcrypt
import tornado.web
from mongo.AssignmentDao import AssignmentDao
# A thread pool to be used for password hashing with bcrypt.
executor = concurrent.futures.ThreadPoolExecutor(2)
def any_author_exists():
        return False


class UserHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("assignment/create_author.html")
    @gen.coroutine
    def post(self):
        print"test"
        if any_author_exists():
            raise tornado.web.HTTPError(400, "author already created")
        hashed_password = yield executor.submit(
            bcrypt.hashpw, tornado.escape.utf8(self.get_argument("password")),
            bcrypt.gensalt())
        email = self.get_argument("email")
        name  = self.get_argument("name")
        print email
        asgdao = AssignmentDao()
        asgdao.create_local_auth(hashed_password, email, name)
        self.set_secure_cookie("blogdemo_user", str(name))
        self.redirect(self.get_argument("next", "/"))
#if __name__ == "__main__":
#    email = "test"
#    name = "name"
#    hashed_password = "hashed_password"
#    asgdao = AssignmentDao()
#    asgdao.create_local_auth(hashed_password, email, name)