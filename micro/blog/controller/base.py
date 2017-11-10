import tornado
from logic.access import context
from logic.access import *

class BaseHandler(tornado.web.RequestHandler):
    role = property(lambda self: self.get_user_role())
    is_teacher = property(lambda self: True)
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self, *args, **kwargs):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')



    def set_acl_role(self):
        context.set_roles_loader([self.role])
    def prepare(self):
        try:
            check_access(self,paccess.keys())
        except:
            self.send_error(403)
    def get_user_role(self):
        return 'admin'
    def get_user(self):
    	print self.role