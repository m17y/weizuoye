import tornado
from logic.access import context

class BaseHandler(tornado.web.RequestHandler):
    role = property(lambda self: self.get_user_role())

    def set_acl_role(self):
        context.set_roles_loader([self.role])
    def prepare(self):
       self.set_acl_role()
        # context.set_roles_loader([cls.role])
    def get_user_role(self):
    	return 'admin'
    def get_user(self):
    	print self.role