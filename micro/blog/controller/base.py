import tornado
from logic.access import context
from logic.access import *

class BaseHandler(tornado.web.RequestHandler):
    role = property(lambda self: self.get_user_role())

    def set_acl_role(self):
        context.set_roles_loader([self.role])
    def prepare(self):
        # self.set_acl_role()
        print paccess
        try:
            check_access(self,paccess.keys())
        except:
            self.send_error(403)
    def get_user_role(self):
        return 'admin'
    def get_user(self):
    	print self.role