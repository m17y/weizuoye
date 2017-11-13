# -*- coding:utf-8 -*-
import hashlib
import tornado.web
from bson import ObjectId

from model.Assignment import *
from logic.access import *
from base import BaseHandler
from logic.access import *



@needcheck()
class UserHandler(BaseHandler):

    def get(self):
        data = User.objects(id=ObjectId(self.uid))
        self.write(dict(data=data.to_json(),status=True,msg='xxx'))

    def post(self):
        user = ag.User()
        kwargs = dict((k,v[-1])for k ,v in self.request.arguments.items())
        user.modelfactory(kwargs)
        status ,msg = user.unique_save()
        self.write(dict(status=status,msg=msg))

    def put(self):
        userid = self.uid
        email = self.get_argument('nickname','')
        password =self.get_argument('nickname','')
        kwargs={'email':email}
        if password:
            kwargs['password'] = password
        User.objects().modify(taskerid="taskerid",id=self.uid,**kwargs)
        self.write(dict(status=True,msg='update success'))

    def delete(self):
        taskerid = self.get_argument('taskerid')
        User.objects(taskerid="taskerid",id=self.uid).delete()
        self.write(dict(status=True,msg='删除成功'))
