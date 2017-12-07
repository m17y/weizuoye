import tornado
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
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

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

    def prepare(self):
        try:
            check_access(self,paccess.keys())
        except:
            self.send_error(403)
    def get_user_role(self):
        return 'admin'
